from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

@api_view(['POST'])
def chatbot_response(request):
    user_message = request.data.get("message", "")
    
    if not os.getenv('OPENAI_API_KEY'):
        return JsonResponse({
            "error": "OpenAI API key not found in environment variables"
        }, status=500)
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ]
        )
        
        return JsonResponse({
            "response": response.choices[0].message.content
        })
    except Exception as e:
        error_message = str(e)
        status_code = 500
        
        if "insufficient_quota" in error_message:
            error_message = "OpenAI API quota exceeded. Please check your billing status."
            status_code = 429
            
        return JsonResponse({
            "error": error_message
        }, status=status_code)