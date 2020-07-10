from django.shortcuts import render
from rest_framework import generics
from .models import UserDetails, Email, Mobile
from .serializers import UserSerializer
from django.http import HttpResponse


class UserListView(generics.ListCreateAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserSerializer
    

class UserDetailsView(generics.RetrieveAPIView):
    #queryset = UserDetails.objects.filter(id=1).select_related('user_mobile').all()
    #queryset=Mobile.objects.all()
    #queryset = UserDetails.objects.select_related('user_id')
    print(queryset)
    #queryset = UserDetails.objects.all().prefetch_related('email')
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

   
