from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .serializers import UserRegistrationSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Todo
from .serializers import TodoSerializer
from .permissions import IsOwner



@api_view(['GET'])
def api_root(request):
     return Response({
          'message': 'Welcome to the Todo API',
          'endpoints': {
                'todos': '/todos/',
          }
     })

class UserRegistrationView(generics.CreateAPIView):
     queryset = User.objects.all()
     serializer_class = UserRegistrationSerializer
     permission_classes = [permissions.AllowAny]


class CustomAuthToken(ObtainAuthToken):
     permission_classes = [permissions.AllowAny]

     def post(self, request, *args, **kwargs):
          serializer = self.serializer_class(data=request.data,
          context={'request': request})

          serializer.is_valid(raise_exception=True)
          user = serializer.validated_data['user']
          token, created = Token.objects.get_or_create(user=user)
          return Response({
               'token': token.key,
               'user_id': user.pk,
               'username': user.username,
               'email': user.email
          }
          )

class TodoListView(generics.ListAPIView):
     serializer_class = TodoSerializer

     def get_queryset(self):
          user = self.request.user
          return Todo.objects.filter(user=user)\
               .select_related('user')
     

class TodoCreateView(generics.CreateAPIView):
     serializer_class = TodoSerializer

     def perform_create(self, serializer):
          serializer.save(user=self.request.user)


class TodoUpdateView(generics.UpdateAPIView):
     serializer_class = TodoSerializer
     permission_classes = [IsOwner]

     def get_queryset(self):
          return Todo.objects.filter(user=self.request.user)
     
class TodoDeleteView(generics.DestroyAPIView):
     serializer_class = TodoSerializer
     permission_classes = [IsOwner]
     
     def get_queryset(self):
          return Todo.objects.filter(user= self.request.user)
