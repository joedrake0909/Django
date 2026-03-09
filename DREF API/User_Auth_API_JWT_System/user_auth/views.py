from rest_framework import status
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated

class RegisterView(APIView):
    permission_classes = [AllowAny]
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
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]  
    def get(self, request):
        return Response({'message': "You accessed a protected endpoint!"})

# Create your views here.
