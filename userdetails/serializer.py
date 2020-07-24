from rest_framework import serializers
import userdetails.models as userdetailmodels
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import authenticate
import login.models as loginmodels
from userprofile.serializer import ProfileSerializer

class EmailSerializer(serializers.ModelSerializer):    
    class Meta:        
        model = userdetailmodels.Email       
        fields = "__all__"

class MobileSerializer(serializers.ModelSerializer):    
    class Meta:        
        model = userdetailmodels.Mobile        
        fields = "__all__"

class ResAddressSerializer(serializers.ModelSerializer):    
    class Meta:        
        model =   userdetailmodels.ResAddress     
        fields = "__all__"
            
class OffAddressSerializer(serializers.ModelSerializer):    
    class Meta:        
        model =   userdetailmodels.OfficeAddress     
        fields = "__all__"

