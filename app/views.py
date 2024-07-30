from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer, LoginSerializer, PromoSerializer
from .models import Promo
from rest_framework.permissions import IsAuthenticated
from .tasks import update_promo_data

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LoginView(APIView):
    serializer_class = LoginSerializer
    def get(self, request):
        return Response({'detail': 'Выполните post запрос с данными от аккаунта'})
    def post(self, request):
        update_promo_data.delay()
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(username=serializer.data['username'], password=serializer.data['password'])
        if user is not None:
            login(request, user)
            return Response({'status': 'ok'})
        return Response({"error": "Неверные данные"}, status=status.HTTP_401_UNAUTHORIZED)


class MainView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        promos = Promo.objects.all()
        serializer = PromoSerializer(promos, many=True)
        return Response(serializer.data)
        