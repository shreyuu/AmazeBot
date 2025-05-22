from django.contrib import admin
from .models import ChatMessage

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('session_id', 'is_user_message', 'short_message', 'timestamp')
    list_filter = ('is_user_message', 'timestamp')
    search_fields = ('session_id', 'message')
    date_hierarchy = 'timestamp'
    
    def short_message(self, obj):
        max_length = 50
        if len(obj.message) > max_length:
            return f"{obj.message[:max_length]}..."
        return obj.message
    
    short_message.short_description = 'Message'
