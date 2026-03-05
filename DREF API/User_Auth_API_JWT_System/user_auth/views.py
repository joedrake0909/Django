from rest_framework import status
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    'message': 'User registered successfully',
                    'user': {
                        'username': user.username,
                        'email': user.email
                    }
                }, status=status.HTTP_201_CREATED
            )



# Create your views here.
