from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Message

def intro_view(request):
    return render(request, 'chat/intro.html')

def chat_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        content = request.POST.get('content')
        if username and content:
            Message.objects.create(username=username, content=content)
        return redirect('chat')

    # Load the most recent 50 messages
    messages = Message.objects.order_by('timestamp')[:50]
    return render(request, 'chat/chat.html', {'messages': messages})

def messages_api(request):
    # Client will pass ?since=<last-id>
    try:
        last_id = int(request.GET.get('since', 0))
    except (TypeError, ValueError):
        last_id = 0

    new_msgs = Message.objects.filter(id__gt=last_id).order_by('timestamp')
    data = [
        {
            'id': m.id,
            'username': m.username,
            'content': m.content,
            'timestamp': m.timestamp.isoformat(),
        }
        for m in new_msgs
    ]
    return JsonResponse(data, safe=False)