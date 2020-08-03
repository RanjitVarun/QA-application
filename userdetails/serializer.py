from rest_framework import serializers
from userdetails.models  import Email,Mobile,ResAddress,OfficeAddress
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import authenticate
from login.models import User
from userprofile.serializer import ProfileSerializer


class EmailSerializer(serializers.ModelSerializer):    
    class Meta:        
        model = Email       
        fields = ("id","email")

class EmailUserSerializer(serializers.ModelSerializer):
    emails=EmailSerializer(many=True, read_only=True)    
    class Meta:        
        model = User      
        fields = ("emails","id")       

class MobileSerializer(serializers.ModelSerializer):    
    class Meta:        
        model = Mobile        
        fields = ("id","mobile")


class MobileUserSerializer(serializers.ModelSerializer):
    mobiles=MobileSerializer(many=True, read_only=True)    
    class Meta:        
        model = User      
        fields = ("mobiles","id") 

class ResAddressSerializer(serializers.ModelSerializer):    
    class Meta:        
        model =   ResAddress     
        fields = ("id","line1","line2","line3","landmark","state","pin")
            
class OffAddressSerializer(serializers.ModelSerializer):    
    class Meta:        
        model =  OfficeAddress     
        fields = ("id","line1","line2","line3","landmark","state","pin")

class AddUserDetailsSerializer(serializers.ModelSerializer):

    email = EmailSerializer(required=False)
    mobile = MobileSerializer(required=False)
    resaddress=ResAddressSerializer(required=False)
    officeaddress=OffAddressSerializer(required=False)

    class Meta:
        model = User
        fields = ('email', 'mobile','resaddress','officeaddress')
