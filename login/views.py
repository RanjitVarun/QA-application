from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
import login.serializer as serializerall
import login.models as loginmodels
from django.contrib.auth import authenticate, login, logout
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import update_last_login
from django.contrib.auth import authenticate
from userdetails.models import Email, Mobile
from rest_framework import serializers

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER


class UserRegistrationView(CreateAPIView):

    serializer_class = serializerall.UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code = status.HTTP_201_CREATED
        response = {
            'success' : 'True',
            'status code' : status_code,
            'message': 'User registered  successfully',
            }
        
        return Response(response, status=status_code)

class UserLoginView(RetrieveAPIView):

    permission_classes = (AllowAny,)
    serializer_class = serializerall.UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(email=request.data['email'], password=request.data['password'])
        if user is None:
            try:
                check=Email.objects.get(email=request.data['email']) 
                user=loginmodels.User.objects.get(id=check.user_id)    

            except Email.DoesNotExist or loginmodels.User.DoesNotExist:
             raise serializers.ValidationError(
                'User with given email and password does not exists'
            )     
        payload = JWT_PAYLOAD_HANDLER(user)
        user_id=payload['user_id']
        jwt_token = JWT_ENCODE_HANDLER(payload)
        update_last_login(None, user)    
        response = {
                'success' : 'True',
                'status code' : status.HTTP_200_OK,
                'message': 'User logged in  successfully',
                'user_id':user_id,
                'token' : jwt_token}    
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)
        

class UserLogoutView(ListAPIView):


    def get(self, request):
        response = {
            'success' : 'True',
            'message': 'User loggedout successfully',
            }
        
        return Response(response)

    