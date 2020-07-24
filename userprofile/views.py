from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from login.serializer import UserRegistrationSerializer
import userprofile.models as profilemodels
from userdetails.models import Email, Mobile, OfficeAddress, ResAddress
from userdetails.serializer import OffAddressSerializer, ResAddressSerializer

class UserProfileView(RetrieveAPIView):

    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    def get(self, request):
        try:
            user_profile = profilemodels.UserProfile.objects.get(user=request.user)
            user_offadd=OfficeAddress.objects.get(user=request.user)
            addserializer=OffAddressSerializer(user_offadd)
            user_resadd=ResAddress.objects.get(user=request.user)
            resserializer=ResAddressSerializer(user_resadd)
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
                    'Office':addserializer.data,
                    'Res':resserializer.data
                    }]
                }

        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'User does not exists',
                'error': str(e)
                }
        return Response(response, status=status_code)
