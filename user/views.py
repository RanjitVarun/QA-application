from django.shortcuts import render
from rest_framework import generics
from .models import UserDetails, Email, Mobile
from .serializers import UserSerializer
from django.http import HttpResponse


class UserListView(generics.ListCreateAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserSerializer
    
class UserDetailsView(generics.RetrieveAPIView):
    queryset=UserDetails.objects.all()
    serializer_class = UserSerializer
    
class UserCreateView(generics.CreateAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserSerializer

class UserUpdateView(generics.UpdateAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserSerializer    

class UserDeleteView(generics.DestroyAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserSerializer    

   
