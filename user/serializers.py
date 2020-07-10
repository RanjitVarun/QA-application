from rest_framework import serializers
from .models import UserDetails, Mobile, Email, EducationRelUser,Education,Course, ResAddress, OfficeAddress, Board

class EmailSerializer(serializers.ModelSerializer):    
    class Meta:        
        model = Email        
        fields = "__all__" 

class MobileSerializer(serializers.ModelSerializer):    
    class Meta:        
        model = Mobile        
        fields = "__all__"    

class EduRelSerializer(serializers.ModelSerializer):    
    class Meta:        
        model =   EducationRelUser     
        fields = "__all__"               

class UserSerializer(serializers.ModelSerializer):
   email = EmailSerializer(many=True, read_only=True)   
   mobile =MobileSerializer(many=True, read_only=True)  
   edu =EduRelSerializer(many=True, read_only=True) 
   class Meta:
        fields = (
            'id',
            'first_name',
            'last_name',
            'DOB',
            'gender',
            'password', 
            'email',
            'mobile',
            'edu'
            
        )
        model = UserDetails


     