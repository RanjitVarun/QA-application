from rest_framework import serializers
from userprofile.models import UserProfile
from login.models import User

class ProfileSerializer(serializers.ModelSerializer):    
    class Meta:        
        model =UserProfile      
        fields =(
            'id','first_name',
            "last_name")

class UserNameSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=128)

class UserNameListSerializer(serializers.ModelSerializer):  
    profile=ProfileSerializer(read_only=True)
    class Meta:        
        model =User    
        fields =("id","profile")