from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
import login.serializer as serializerall
from login.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import update_last_login
from django.contrib.auth import authenticate,login
from userdetails.models import Email, Mobile
from rest_framework import serializers
from django.contrib.sessions.backends.db import SessionStore
from django.core.exceptions import PermissionDenied 
from django.contrib.auth.hashers import check_password
from django.http import JsonResponse

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

class UserLoginView(CreateAPIView):

    permission_classes = (AllowAny,)
    serializer_class = serializerall.UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(email=request.data['email'], password=request.data['password'])
        if user is None:
            try:
                check=Email.objects.get(email=request.data['email']) 
                user=User.objects.get(id=check.user_id) 
                here=user.check_password(request.data['password'])
                if here is False:
                    raise serializers.ValidationError(
                  'password does not exists'
                  )   
            except Email.DoesNotExist or User.DoesNotExist:
               raise serializers.ValidationError(
                'User with given email and password does not exists'
            )     

        payload = JWT_PAYLOAD_HANDLER(user)
        user_id=payload['user_id']
        jwt_token = JWT_ENCODE_HANDLER(payload)
        if request.session['_auth_user_id'] == user_id:
            raise serializers.ValidationError(
                  'User already logged In'
                  )   
        else:
             pass   
        login(request,user)
        update_last_login(None, user)    
        response = {
                'success' : 'True',
                'status code' : status.HTTP_200_OK,
                'message': 'User logged in  successfully',
                'user_id':user_id,
                'token' : jwt_token}    
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)
        

class UserLogoutView(CreateAPIView):

    def post(self, request):
        try:
          request.session['_auth_user_id']=None
          request.session['_auth_user_hash']=None
        except KeyError:
         pass
        response = {
            'success' : 'True',
            'message': 'User loggedout successfully',
            'session':request.session
            }
        
        return Response(response)


# def handler404(request,exception):
#     print("calling")
#     return JsonResponse({'detail': "The resource was not found",'status_code': 404}, status=404)
   

# def handler500(request):
#     return JsonResponse({'detail': "Internal Server Error",'status_code': 500}, status=500)
    