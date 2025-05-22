from django.test import TestCase, Client
from django.urls import reverse
from .models import ChatMessage
import uuid
import json

# Create your tests here.

class ChatMessageModelTest(TestCase):
    def setUp(self):
        self.session_id = str(uuid.uuid4())
        self.user_msg = ChatMessage.objects.create(
            session_id=self.session_id,
            is_user_message=True,
            message="Hello, bot!"
        )
        self.bot_msg = ChatMessage.objects.create(
            session_id=self.session_id,
            is_user_message=False,
            message="Hello, human!"
        )
    
    def test_chat_message_creation(self):
        """Test that ChatMessage instances are created correctly"""
        self.assertEqual(ChatMessage.objects.count(), 2)
        self.assertEqual(self.user_msg.message, "Hello, bot!")
        self.assertTrue(self.user_msg.is_user_message)
        self.assertEqual(self.bot_msg.message, "Hello, human!")
        self.assertFalse(self.bot_msg.is_user_message)

    def test_chat_message_str(self):
        """Test the string representation of ChatMessage"""
        self.assertEqual(str(self.user_msg), "User: Hello, bot!...")
        self.assertEqual(str(self.bot_msg), "Bot: Hello, human!...")


class ConversationHistoryTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.session_id = str(uuid.uuid4())
        
        # Create some test messages
        ChatMessage.objects.create(
            session_id=self.session_id,
            is_user_message=True,
            message="Hello"
        )
        ChatMessage.objects.create(
            session_id=self.session_id,
            is_user_message=False,
            message="Hi there!"
        )
        ChatMessage.objects.create(
            session_id=self.session_id,
            is_user_message=True,
            message="How are you?"
        )
        ChatMessage.objects.create(
            session_id=self.session_id,
            is_user_message=False,
            message="I'm doing well, thanks!"
        )
    
    def test_get_conversation_history(self):
        """Test retrieving conversation history endpoint"""
        url = reverse('conversation-history', kwargs={'session_id': self.session_id})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(len(data['history']), 4)
        self.assertEqual(data['session_id'], self.session_id)
        self.assertEqual(data['history'][0]['message'], "Hello")
        self.assertTrue(data['history'][0]['is_user'])
    
    def test_clear_conversation(self):
        """Test clearing conversation history"""
        url = reverse('chatbot-response')
        response = self.client.post(
            url, 
            {'session_id': self.session_id, 'clear_conversation': True},
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ChatMessage.objects.filter(session_id=self.session_id).count(), 0)
