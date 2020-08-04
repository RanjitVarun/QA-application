from django.shortcuts import render
from rest_framework import generics, serializers, views, exceptions,status
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from userdetails.models  import Email,Mobile,ResAddress,OfficeAddress
import userdetails.serializer as serializer
from userdetails.serializer import EmailSerializer, MobileSerializer, AddUserDetailsSerializer
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
from login.models import User


class EmailCreateView(generics.CreateAPIView):
    serializer_class = serializer.EmailSerializer  

class MobileCreateView(generics.CreateAPIView):
    serializer_class = serializer.MobileSerializer   
 
class EmailDeleteView(generics.DestroyAPIView):
    queryset = Email.objects.all()
    serializer_class = serializer.EmailSerializer

class MobileDeleteView(generics.DestroyAPIView):
    queryset = Mobile.objects.all()
    serializer_class = serializer.MobileSerializer 
    
class OffAddressUpdateView(generics.UpdateAPIView):
    queryset = OfficeAddress.objects.all()
    serializer_class = serializer.OffAddressSerializer

class ResAddressUpdateView(generics.UpdateAPIView):
    queryset = ResAddress.objects.all()
    serializer_class = serializer.ResAddressSerializer 
 
class AddUserDetailsView(generics.ListCreateAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = serializer.AddUserDetailsSerializer
    authentication_class = JSONWebTokenAuthentication

    def get(self, request):
        try:
            res_address = ResAddress.objects.get(user=request.user)
            res_data=serializer.ResAddressSerializer(res_address)
            off_address = OfficeAddress.objects.get(user=request.user)
            office_data=serializer.OffAddressSerializer(off_address)
            user=User.objects.get(email=request.user)
            email_data=serializer.EmailUserSerializer(user)
            mobile_data=serializer.MobileUserSerializer(user)
            status_code = status.HTTP_200_OK
            response = {
                'success': 'true',
                'status code': status_code,
                'message': 'User Details fetched successfully',
                 'data': [{
                     'email':email_data.data,
                     'mobile':mobile_data.data,
                'residential':res_data.data,
                'office':office_data.data }]
                }

        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'User Details cannot be fetched',
                'error': str(e)
                }
        return Response(response, status=status_code)

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = User.objects.get(email=request.user)
            email_data=serializer.validated_data.pop('email')
            mobile_data=serializer.validated_data.pop('mobile')
            res_data=serializer.validated_data.pop('resaddress')
            office_data=serializer.validated_data.pop('officeaddress')
            Email.objects.create(user=user,email=email_data['email'])
            Mobile.objects.create(user=user,mobile=mobile_data['mobile'])
            ResAddress.objects.create(
                user=user,
                line1=res_data['line1'],
                line2=res_data['line2'],
                line3=res_data['line3'],
                landmark=res_data['landmark'],
                state=res_data['state'],
                pin=res_data['pin']
            )
            OfficeAddress.objects.create(
                user=user,
                line1=office_data['line1'],
                line2=office_data['line2'],
                line3=office_data['line3'],
                landmark=office_data['landmark'],
                state=office_data['state'],
                pin=office_data['pin']
            )
            status_code = status.HTTP_200_OK
            response = {
                'success': 'true',
                'status code': status_code,
                'message': 'User Details Added successfully',
                }

        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'User Details cannot be updated',
                'error': str(e)
                }
        return Response(response, status=status_code)


        

      




  


   
    
    

