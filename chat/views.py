from django.shortcuts import render,redirect
from .models import Message
from django.http import HttpResponse
from django.core.management import call_command


# Create your views hee.
def migrate_view(request):
    call_command('migrate')
    return HttpResponse("Migrations applied.")


def intro_view(request):
    return render(request, 'chat/intro.html')

def chat_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        content = request.POST.get('content')
        if username and content:
            Message.objects.create(username=username, content=content)
        return redirect('chat')  # Prevents resubmission on refresh

    messages = Message.objects.order_by('-timestamp')[:50]  # Latest 50 messages
    return render(request, 'chat/chat.html', {'messages': messages})
