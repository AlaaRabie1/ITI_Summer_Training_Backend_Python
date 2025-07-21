from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        
        if User.objects.filter(username=username).exists():
            return Response({"error":"username already exists"}, status=400)
        
        user = User.objects.create_user(username=username, password=password)
        return Response({"message": "User created successfully"}, status=201)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        
        user = authenticate(username=username, password=password)
        
        if user is None:
            return Response({"error":"invalid Credentials!"}, status=401)
        
        refresh = RefreshToken.for_user(user)
        
        return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            })
