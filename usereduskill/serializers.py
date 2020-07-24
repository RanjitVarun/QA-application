from rest_framework import serializers
import usereduskill.models as models
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import authenticate
import login.models as loginmodels

class EducationSerializer(serializers.ModelSerializer):    
    class Meta:        
        model =   models.Education     
        fields = "__all__"

class CourseSerializer(serializers.ModelSerializer):    
    class Meta:        
        model =   models.Course     
        fields = "__all__"      
        
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
    class Meta:        
        model =   models.skillsetRel    
        fields = "__all__"
    
 



       









