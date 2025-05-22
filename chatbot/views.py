from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
import requests
import os
from pathlib import Path
from dotenv import load_dotenv
import logging
from django.core.cache import cache
from rest_framework.throttling import UserRateThrottle
import time
import json
import uuid
from .throttling import ChatbotRateThrottle
from .models import ChatMessage

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Build paths and load environment
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR / '.env'
load_dotenv(dotenv_path=ENV_FILE)
logger.info(f"Looking for .env file at: {ENV_FILE}")

# Verify API key is loaded
api_key = os.getenv('HUGGINGFACE_API_KEY')
if not api_key:
    logger.error("HUGGINGFACE_API_KEY not found in environment variables")
    raise ValueError("HUGGINGFACE_API_KEY not found in environment variables")
logger.info("API key loaded successfully")


def make_api_request_with_retry(url, headers, payload, max_retries=3, delay=2):
    """Helper function to handle retries with exponential backoff"""
    for attempt in range(max_retries):
        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            if attempt == max_retries - 1:
                logger.error(f"API request failed after {max_retries} attempts: {str(e)}")
                raise
            wait_time = delay * (2 ** attempt)
            logger.warning(f"Attempt {attempt + 1} failed. Retrying in {wait_time} seconds...")
            time.sleep(wait_time)


def format_conversation_context(session_id, max_messages=5):
    """Get the conversation history for context"""
    # Get the last few messages for context, ordered by timestamp
    recent_messages = ChatMessage.objects.filter(
        session_id=session_id
    ).order_by('-timestamp')[:max_messages]
    
    # Format the conversation context for the API
    conversation = []
    for msg in reversed(recent_messages):
        conversation.append({
            "role": "user" if msg.is_user_message else "assistant",
            "content": msg.message
        })
    
    return conversation


@api_view(['POST'])
def chatbot_response(request):
    throttle = ChatbotRateThrottle()
    if not throttle.allow_request(request, None):
        logger.warning("Rate limit exceeded")
        return JsonResponse({
            "error": "Rate limit exceeded",
            "detail": "Please wait a moment before trying again"
        }, status=429)

    # Get or create session ID
    session_id = request.data.get("session_id", "")
    if not session_id:
        session_id = str(uuid.uuid4())
        logger.info(f"Created new session: {session_id}")

    # Check if this is a clear conversation request
    if request.data.get("clear_conversation", False):
        ChatMessage.objects.filter(session_id=session_id).delete()
        logger.info(f"Cleared conversation history for session: {session_id}")
        return JsonResponse({
            "session_id": session_id,
            "message": "Conversation history cleared"
        })

    # Get user message
    user_message = request.data.get("message", "")
    if not user_message:
        return JsonResponse({
            "error": "Invalid request",
            "detail": "Message cannot be empty"
        }, status=400)
    
    try:
        # Save user message to database
        ChatMessage.objects.create(
            session_id=session_id,
            is_user_message=True,
            message=user_message
        )
        
        # Check cache first
        cache_key = f"chat_response_{session_id}_{hash(user_message)}"
        cached_response = cache.get(cache_key)
        if cached_response:
            logger.info("Returning cached response")
            # Save cached bot response to database
            ChatMessage.objects.create(
                session_id=session_id,
                is_user_message=False,
                message=cached_response
            )
            return JsonResponse({
                "response": cached_response,
                "session_id": session_id
            })

        logger.info("Making API request to Hugging Face")
        API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
        headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"}
        
        # Get conversation history to provide context
        conversation_history = format_conversation_context(session_id)
        
        # Use conversation history if available
        if conversation_history:
            # For Blenderbot, we'll just use the most recent history in the prompt
            # Format varies by model - adjust as needed
            context = " ".join([msg["content"] for msg in conversation_history])
            payload = {"inputs": f"{context} {user_message}".strip()}
        else:
            payload = {"inputs": user_message}

        # Make API request with retry logic
        response_data = make_api_request_with_retry(API_URL, headers, payload)
        response_content = response_data[0]['generated_text']

        # Save bot response to database
        ChatMessage.objects.create(
            session_id=session_id,
            is_user_message=False,
            message=response_content
        )

        # Cache successful response
        cache.set(cache_key, response_content, timeout=300)  # Cache for 5 minutes
        
        return JsonResponse({
            "response": response_content,
            "session_id": session_id
        })

    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        return JsonResponse({
            "error": "Service unavailable",
            "detail": "Please try again later",
            "session_id": session_id
        }, status=503)


@api_view(['GET'])
def get_conversation_history(request, session_id):
    """Endpoint to retrieve conversation history for a session"""
    try:
        messages = ChatMessage.objects.filter(
            session_id=session_id
        ).order_by('timestamp')
        
        history = [{
            "message": msg.message,
            "is_user": msg.is_user_message,
            "timestamp": msg.timestamp.isoformat()
        } for msg in messages]
        
        return JsonResponse({
            "session_id": session_id,
            "history": history
        })
    except Exception as e:
        logger.error(f"Error retrieving conversation history: {str(e)}")
        return JsonResponse({
            "error": "Failed to retrieve history",
            "detail": str(e)
        }, status=500)