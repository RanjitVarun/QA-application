from rest_framework import serializers
from userprofile.models import UserProfile

class ProfileSerializer(serializers.ModelSerializer):    
    class Meta:        
        model =UserProfile      
        fields =(
            'id','first_name',
            "last_name")


class NameSerializer(serializers.ModelSerializer):    
    class Meta:        
        model =UserProfile      
        fields =('first_name',
            "last_name")