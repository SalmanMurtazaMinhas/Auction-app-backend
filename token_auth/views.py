from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView, ListAPIView
from .models import User
from .serializer import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer