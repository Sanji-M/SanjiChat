from django.urls import path
from .views import chat_view, intro_view

urlpatterns = [
    path('', intro_view, name='intro'),
    path('chat/', chat_view, name='chat'),
]