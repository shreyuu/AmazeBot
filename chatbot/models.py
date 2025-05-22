from django.db import models
from django.utils import timezone

# Create your models here.

class ChatMessage(models.Model):
    """Model to store chat messages and maintain conversation history"""
    
    # Optional session identifier for anonymous users
    session_id = models.CharField(max_length=100, db_index=True)
    
    # User or bot message
    is_user_message = models.BooleanField(default=True)
    
    # Message content
    message = models.TextField()
    
    # Timestamp
    timestamp = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['timestamp']
    
    def __str__(self):
        sender = "User" if self.is_user_message else "Bot"
        return f"{sender}: {self.message[:50]}..."
