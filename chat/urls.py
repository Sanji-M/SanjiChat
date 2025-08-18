from django.urls import path
from .views import chat_view, intro_view, migrate_view  # 👈 Add migrate_view

urlpatterns = [
    path('', intro_view, name='intro'),
    path('chat/', chat_view, name='chat'),
    path('migrate/', migrate_view, name='migrate'),  # 👈 Add this line
]