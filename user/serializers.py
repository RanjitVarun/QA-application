from rest_framework import serializers
from .models import UserDetails


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'first_name',
            'last_name',
            'DOB',
            'gender',
            'password',  
        )
        model = UserDetails