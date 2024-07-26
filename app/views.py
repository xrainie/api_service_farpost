from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer, LoginSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LoginView(APIView):
    serializer_class = LoginSerializer
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(username=serializer.data['username'], password=serializer.data['password'])
        if user is not None:
            login(request, user)
            return Response({'status': 'ok'})
        return Response({"error": "Неверные данные"}, status=status.HTTP_401_UNAUTHORIZED)