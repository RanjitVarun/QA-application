from rest_framework import serializers
from .models import UserDetails, Mobile, Email, EducationRelUser,Education,Course, ResAddress, OfficeAddress, Board,Skillset,skillsetRel

class EmailSerializer(serializers.ModelSerializer):    
    class Meta:        
        model = Email        
        fields = "__all__" 

class MobileSerializer(serializers.ModelSerializer):    
    class Meta:        
        model = Mobile        
        fields = "__all__"    

class ResAddressSerializer(serializers.ModelSerializer):    
    class Meta:        
        model =   ResAddress     
        fields = "__all__"

class OffAddressSerializer(serializers.ModelSerializer):    
    class Meta:        
        model =   OfficeAddress     
        fields = "__all__"  

class EducationSerializer(serializers.ModelSerializer):    
    class Meta:        
        model =   Education     
        fields = "__all__"

class CourseSerializer(serializers.ModelSerializer):    
    class Meta:        
        model =   Course     
        fields = "__all__"        
        
class BoardSerializer(serializers.ModelSerializer):    
    class Meta:        
        model =   Board     
        fields ="__all__"

class BoardCourseSerializer(serializers.Serializer):
    board = BoardSerializer(many=True, read_only=True)
    course = CourseSerializer(many=True, read_only=True)
    degree= EducationSerializer(many=True, read_only=True)
    class Meta:          
        fields = "__all__" 
     
class EduRelSerializer(serializers.ModelSerializer):
    class Meta:        
        model =   EducationRelUser    
        fields = ("course","board","degree")  
        depth = 1 

class SkillSerializer(serializers.ModelSerializer):
    class Meta:        
        model =   Skillset    
        fields = "__all__"

class SkillsetSerializer(serializers.ModelSerializer):
    class Meta:        
        model =   skillsetRel    
        fields = "__all__"
        depth = 1 

class UserSerializer(serializers.ModelSerializer):
   email = EmailSerializer(many=True, read_only=True)   
   mobile =MobileSerializer(many=True, read_only=True)  
   resaddress =ResAddressSerializer(many=True, read_only=True) 
   offaddress =OffAddressSerializer(many=True, read_only=True)
   user_relation=EduRelSerializer(many=True, read_only=True)
   user_skill=SkillsetSerializer(many=True, read_only=True)
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
            'resaddress',
            'offaddress',
            'user_relation', 
            'user_skill'
        )
        model = UserDetails
       


     