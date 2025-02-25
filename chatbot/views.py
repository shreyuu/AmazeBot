from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from openai import OpenAI
import os
from pathlib import Path
from dotenv import load_dotenv
import logging
import time
from django.core.cache import cache
from rest_framework.throttling import UserRateThrottle
from tenacity import retry, stop_after_attempt, wait_exponential

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Build paths and load environment
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR / '.env'
load_dotenv(dotenv_path=ENV_FILE)
logger.info(f"Looking for .env file at: {ENV_FILE}")

# Verify API key is loaded
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    logger.error("OPENAI_API_KEY not found in environment variables")
    raise ValueError("OPENAI_API_KEY not found in environment variables")
logger.info("API key loaded successfully")

# Initialize OpenAI client with retry mechanism
@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=4, max=10)
)
def create_chat_completion(messages):
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    return client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

class ChatbotRateThrottle(UserRateThrottle):
    rate = '3/minute'  # Reduced rate to prevent quota issues

@api_view(['POST'])
def chatbot_response(request):
    throttle = ChatbotRateThrottle()
    if not throttle.allow_request(request, None):
        return JsonResponse({
            "error": "Rate limit exceeded",
            "detail": "Too many requests. Please try again later."
        }, status=429)

    user_message = request.data.get("message", "")
    if not user_message:
        return JsonResponse({
            "error": "Invalid request",
            "detail": "Message cannot be empty"
        }, status=400)
    
    try:
        # Check cache first
        cache_key = f"chatbot_response_{hash(user_message)}"
        cached_response = cache.get(cache_key)
        if cached_response:
            logger.info("Returning cached response")
            return JsonResponse({"response": cached_response})

        logger.info("Attempting to create chat completion")
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message}
        ]
        
        response = create_chat_completion(messages)
        response_content = response.choices[0].message.content
        
        # Cache successful responses for 10 minutes
        cache.set(cache_key, response_content, 600)
        
        logger.info("Successfully received response from OpenAI")
        return JsonResponse({"response": response_content})
        
    except Exception as e:
        error_message = str(e)
        logger.error(f"OpenAI API error: {error_message}")
        
        if "insufficient_quota" in error_message:
            logger.error("Quota exceeded error detected")
            return JsonResponse({
                "error": "Service temporarily unavailable",
                "detail": "We're experiencing high demand. Please try again later."
            }, status=503)
        
        return JsonResponse({
            "error": "Internal server error",
            "detail": "An unexpected error occurred"
        }, status=500)