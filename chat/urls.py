from django.urls import path
from .views import intro_view, chat_view, messages_api

urlpatterns = [
    path('', intro_view, name='intro'),
    path('chat/', chat_view, name='chat'),
    path('api/messages/', messages_api, name='messages_api'),
]