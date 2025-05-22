from django.urls import path
from .views import chatbot_response, get_conversation_history

urlpatterns = [
    path("chat/", chatbot_response, name="chatbot-response"),
    path("history/<str:session_id>/", get_conversation_history, name="conversation-history"),
]
