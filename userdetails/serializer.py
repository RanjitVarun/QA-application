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

# class UserDetailsSerializer(serializers.ModelSerializer):
# #    email = EmailSerializer(many=True, read_only=True)   
# #    mobile =MobileSerializer(many=True, read_only=True)  
#    userprofile=ProfileSerializer(many=True, read_only=True)
# #    resaddress =ResAddressSerializer(many=True, read_only=True) 
# #    offaddress =OffAddressSerializer(many=True, read_only=True)
   
#    class Meta:
#         fields = (
            
#             'userprofile',
#             # 'email',
#             # 'mobile',
#             # 'resaddress',
#             # 'offaddress',
            
#         )
#         model = loginmodels.User