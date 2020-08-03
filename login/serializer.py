from rest_framework import serializers
from userprofile.models import UserProfile
from userdetails.models import Email, Mobile
from login.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('first_name','last_name', 'phone_number', 'age', 'gender')

class UserRegistrationSerializer(serializers.ModelSerializer):

    profile = ProfileSerializer(required=False)

    class Meta:
        model = User
        fields = ('email', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}  

class UserLoginSerializer(serializers.Serializer):

    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
