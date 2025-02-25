from rest_framework.throttling import UserRateThrottle

class ChatbotRateThrottle(UserRateThrottle):
    rate = '10/second'  # Allow 10 requests per second