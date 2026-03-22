from django.urls import path
from .import views

urlpatterns = [
    path('',views.api_root, name='api-root'),
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('login/', views.CustomAuthToken.as_view(), name='login'),

    path('todos/', views.TodoListView.as_view(), name='todo-list'),
    path('todos/create/', views.TodoCreateView.as_view(), name='todo-create'),
    path('todos/<int:pk>/update/', views.TodoUpdateView.as_view(), name='todo-update'),
    path('todos/<int:pk>/delete/', views.TodoDeleteView.as_view(), name='todo-delete'),
]