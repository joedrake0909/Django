from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .serializers import UserRegistrationSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


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

