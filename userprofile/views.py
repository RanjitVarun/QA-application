from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import RetrieveAPIView, CreateAPIView , UpdateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from login.serializer import UserRegistrationSerializer
from userprofile.models import UserProfile
from userdetails.models import Email, Mobile, OfficeAddress, ResAddress
from userprofile.serializer import UserNameSerializer, UserNameListSerializer
from login.models import User

class UserProfileView(RetrieveAPIView):

    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    def get(self, request):
        try:
            user_profile = UserProfile.objects.get(user=request.user)
            status_code = status.HTTP_200_OK
            response = {
                'success': 'true',
                'status code': status_code,
                'message': 'User profile fetched successfully',
                'data': [{
                    'first_name': user_profile.first_name,
                    'last_name': user_profile.last_name,
                    'phone_number': user_profile.phone_number,
                    'age': user_profile.age,
                    'gender': user_profile.gender,
                    
                    }]
                }

        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'User Profile does not exists',
                'error': str(e)
                }
        return Response(response, status=status_code)


class UserNameUpdateView(UpdateAPIView):

    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    serializer_class = UserNameSerializer

    def put(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        #user_profile= UserProfile.objects.get(user=request.user)
        user=UserProfile.objects.update_first_name(request.user,serializer.data['first_name'])
        status_code = status.HTTP_200_OK
        response = {
            'success' : 'True',
            'status code' : status_code,
            'message': 'User firstname changed successfully',
            }
        
        return Response(response, status=status_code)


class UserNameList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserNameListSerializer 
