from django.urls import path
from . import views

urlpatterns = [
    path('room/',views.index, name='index' ),
    path('<slug:slug>/', views.chatroom, name='chatroom' ),
]