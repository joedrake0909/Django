from django.urls import path
from .import views

urlpatterns = [
    path('',views.api_root, name='api-root'),
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('login/', views.CustomAuthToken.as_view(), name='login'),
]