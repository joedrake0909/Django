from django.shortcuts import render
from .models import ChatRoom

# Create your views here.
def index(request):
    chatrooms = ChatRoom.objects.all()
    return render(request, 'myapp/index.html', {'chatrooms': chatrooms})

def chatroom(request, slug):
    chatroom = ChatRoom.objects.get(slug=slug)
    return render(request, 'myapp/room.html', {'chatroom':chatroom})
