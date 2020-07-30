from rest_framework import serializers
from usereducationskill.models import Board,Course,Education,EducationRelUser,Skillset,skillsetRel
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import authenticate
from login.models import User

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

class EduSerializer(serializers.ModelSerializer):
    class Meta:        
        model =   EducationRelUser    
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

class SkillRelSerializer(serializers.ModelSerializer):
    skill=SkillSerializer()
    class Meta:        
        model =   skillsetRel    
        fields = ("user","skill")       
     
    




       









