from rest_framework import serializers
import userdetails.models as userdetailmodels
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import authenticate
import login.models as loginmodels
from userprofile.serializer import ProfileSerializer

class EmailSerializer(serializers.ModelSerializer):    
    class Meta:        
        model = userdetailmodels.Email       
        fields = ("id","email")

class EmailUserSerializer(serializers.ModelSerializer):
    emails=EmailSerializer(many=True, read_only=True)    
    class Meta:        
        model = loginmodels.User      
        fields = ("emails","id")       

class MobileSerializer(serializers.ModelSerializer):    
    class Meta:        
        model = userdetailmodels.Mobile        
        fields = ("id","mobile")

class MobileUserSerializer(serializers.ModelSerializer):
    mobiles=MobileSerializer(many=True, read_only=True)    
    class Meta:        
        model = loginmodels.User      
        fields = ("mobiles","id") 

class ResAddressSerializer(serializers.ModelSerializer):    
    class Meta:        
        model =   userdetailmodels.ResAddress     
        fields = "__all__"
            
class OffAddressSerializer(serializers.ModelSerializer):    
    class Meta:        
        model =   userdetailmodels.OfficeAddress     
        fields = "__all__"

