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

class ChatbotRateThrottle(UserRateThrottle):
    rate = '1/second'  # Adjust rate limit to be more conservative

def make_api_request_with_retry(url, headers, payload, max_retries=3, delay=2):
    """Helper function to handle retries with exponential backoff"""
    for attempt in range(max_retries):
        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            if attempt == max_retries - 1:
                raise
            wait_time = delay * (2 ** attempt)
            logger.warning(f"Attempt {attempt + 1} failed. Retrying in {wait_time} seconds...")
            time.sleep(wait_time)

@api_view(['POST'])
def chatbot_response(request):
    throttle = ChatbotRateThrottle()
    if not throttle.allow_request(request, None):
        logger.warning("Rate limit exceeded")
        return JsonResponse({
            "error": "Rate limit exceeded",
            "detail": "Please wait a moment before trying again"
        }, status=429)

    user_message = request.data.get("message", "")
    if not user_message:
        return JsonResponse({
            "error": "Invalid request",
            "detail": "Message cannot be empty"
        }, status=400)
    
    try:
        # Check cache first
        cache_key = f"chat_response_{hash(user_message)}"
        cached_response = cache.get(cache_key)
        if cached_response:
            logger.info("Returning cached response")
            return JsonResponse({"response": cached_response})

        logger.info("Making API request to Hugging Face")
        API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
        headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"}
        payload = {"inputs": user_message}

        # Make API request with retry logic
        response_data = make_api_request_with_retry(API_URL, headers, payload)
        response_content = response_data[0]['generated_text']

        # Cache successful response
        cache.set(cache_key, response_content, timeout=300)  # Cache for 5 minutes
        
        return JsonResponse({"response": response_content})

    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        return JsonResponse({
            "error": "Service unavailable",
            "detail": "Please try again later"
        }, status=503)