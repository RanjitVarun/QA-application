from django.shortcuts import render
from rest_framework import generics, serializers, views, exceptions,status
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
import userdetails.models as model
import userdetails.serializer as serializer
from django.shortcuts import get_object_or_404
from rest_framework import permissions, status
from django.db import Error
from login.models import User
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class EmailCreateView(generics.ListCreateAPIView):
    queryset = model.Email.objects.all()
    serializer_class = serializer.EmailSerializer  

class MobileCreateView(generics.CreateAPIView):
    queryset = model.Mobile.objects.all()
    serializer_class = serializer.MobileSerializer    

class EmailDeleteView(generics.DestroyAPIView):
    queryset = model.Email.objects.all()
    serializer_class = serializer.EmailSerializer

class MobileDeleteView(generics.DestroyAPIView):
    queryset = model.Mobile.objects.all()
    serializer_class = serializer.MobileSerializer 

class OffAddressCreateView(generics.CreateAPIView):
    queryset = model.OfficeAddress.objects.all()
    serializer_class = serializer.OffAddressSerializer
    
class OffAddressUpdateView(generics.UpdateAPIView):
    queryset = model.OfficeAddress.objects.all()
    serializer_class = serializer.OffAddressSerializer

class OffAddressDeleteView(generics.DestroyAPIView):
    queryset = model.OfficeAddress.objects.all()
    serializer_class = serializer.OffAddressSerializer

class ResAddressCreateView(generics.CreateAPIView):
    queryset = model.ResAddress.objects.all()
    serializer_class = serializer.ResAddressSerializer  

class ResAddressUpdateView(generics.UpdateAPIView):
    queryset = model.ResAddress.objects.all()
    serializer_class = serializer.ResAddressSerializer 

class ResAddressDeleteView(generics.DestroyAPIView):
    queryset = model.ResAddress.objects.all()
    serializer_class = serializer.ResAddressSerializer    


class ResAddressView(RetrieveAPIView):

    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    def get(self, request):
        try:
            user_address = model.ResAddress.objects.get(user=request.user)
            serialize=serializer.ResAddressSerializer(user_address)
            status_code = status.HTTP_200_OK
            response = {
                'success': 'true',
                'status code': status_code,
                'message': 'User profile fetched successfully',
                'data': [{
                    'address':serialize.data }] }

        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'No address added for this user',
                'error': str(e)
                }
        return Response(response, status=status_code)


class OfficeAddressView(RetrieveAPIView):

    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    def get(self, request):
        try:
            user_address = model.OfficeAddress.objects.get(user=request.user)
            serialize=serializer.OffAddressSerializer(user_address)
            status_code = status.HTTP_200_OK
            response = {
                'success': 'true',
                'status code': status_code,
                'message': 'User profile fetched successfully',
                'data': [{
                'address':serialize.data }]}

        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'No address added for this user',
                'error': str(e)
                }
        return Response(response, status=status_code)




        

      




  


   
    
    

