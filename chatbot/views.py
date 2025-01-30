from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

# Create your views here.
@api_view(['POST'])
def chatbot_response(request):
    user_message = request.data.get("message", "")
    
    response = openai.Completion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user", "content": user_message}],
    )
    
    return JsonResponse({"response": response["choices"][0]["message"]["content"]})