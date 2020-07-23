from rest_framework import serializers
import userprofile.models as profilemodels
import login.models as loginmodels
from userdetails.models import Email, Mobile
from login.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = profilemodels.UserProfile
        fields = ('first_name', 'last_name', 'phone_number', 'age', 'gender')

class UserRegistrationSerializer(serializers.ModelSerializer):

    profile = UserSerializer(required=False)

    class Meta:
        model = loginmodels.User
        fields = ('email', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = loginmodels.User.objects.create_user(**validated_data)
        profilemodels.UserProfile.objects.create(
            user=user,
            first_name=profile_data['first_name'],
            last_name=profile_data['last_name'],
            phone_number=profile_data['phone_number'],
            age=profile_data['age'],
            gender=profile_data['gender']
        )
        return user

class UserLoginSerializer(serializers.Serializer):

    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
