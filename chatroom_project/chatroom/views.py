from django.shortcuts import render
from .models import Message

def create_message(request):
    if request.method == 'POST':
        sender = request.user  # Assuming you have authentication set up
        content = request.POST.get('content')
        message = Message(sender=sender, content=content)
        message.save()
        # Additional logic or redirection after saving the message

    messages = Message.objects.all()  # Retrieve all messages from the database
    context = {'messages': messages}
    return render(request, 'chat.html', context)
