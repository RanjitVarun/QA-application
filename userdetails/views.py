from django.shortcuts import render
from rest_framework import generics, serializers, views, exceptions,status
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
import userdetails.models as model
import userdetails.serializer as serializer
from django.shortcuts import get_object_or_404
from rest_framework import permissions, status

class EmailCreateView(generics.ListCreateAPIView):
    queryset = model.Email.objects.all()
    serializer_class = serializer.EmailSerializer

class MobileCreateView(generics.ListCreateAPIView):
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









        

      




  


   
    
    

