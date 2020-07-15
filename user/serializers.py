from rest_framework import serializers
import user.models as models

class EmailSerializer(serializers.ModelSerializer):    
    class Meta:        
        model = models.Email       
        fields = "__all__"

class MobileSerializer(serializers.ModelSerializer):    
    class Meta:        
        model = models.Mobile        
        fields = "__all__"

class ResAddressSerializer(serializers.ModelSerializer):    
    class Meta:        
        model =   models.ResAddress     
        fields = "__all__"
            
class OffAddressSerializer(serializers.ModelSerializer):    
    class Meta:        
        model =   models.OfficeAddress     
        fields = "__all__"

class EducationSerializer(serializers.ModelSerializer):    
    class Meta:        
        model =   models.Education     
        fields = "__all__"

class CourseSerializer(serializers.ModelSerializer):    
    class Meta:        
        model =   models.Course     
        fields = ("course","degree_id")        
        
class BoardSerializer(serializers.ModelSerializer):    
    class Meta:        
        model =   models.Board     
        fields ="__all__"

class BoardCourseSerializer(serializers.Serializer):
    board = BoardSerializer(many=True, read_only=True)
    course = CourseSerializer(many=True, read_only=True)
    degree= EducationSerializer(many=True, read_only=True)
    class Meta:          
        fields = "__all__"        
     
class EduRelSerializer(serializers.ModelSerializer):
    class Meta:        
        model =   models.EducationRelUser    
        fields = ("course","board","degree")  
        depth = 1 

class SkillSerializer(serializers.ModelSerializer):
    class Meta:        
        model =   models.Skillset    
        fields = "__all__"

class SkillsetSerializer(serializers.ModelSerializer):
    skill=SkillSerializer(many=True, read_only=True) 
    class Meta:        
        model =   models.skillsetRel    
        fields = "__all__"
    
class SkillsetRelSerializer(serializers.ModelSerializer):
    skill=SkillSerializer(many=True, read_only=True) 
    class Meta:        
        model =   models.skillsetRel    
        fields = "__all__" 
        depth=1   

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:        
        model =   models.UserDetails   
        fields = "__all__" 

class UserSerializer(serializers.ModelSerializer):
   email = EmailSerializer(many=True, read_only=True)   
   mobile =MobileSerializer(many=True, read_only=True)  
   resaddress =ResAddressSerializer(many=True, read_only=True) 
   offaddress =OffAddressSerializer(many=True, read_only=True)
   user_relation=EduRelSerializer(many=True, read_only=True)
   user_skill=SkillsetRelSerializer(many=True, read_only=True)
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
        model = models.UserDetails
       


     