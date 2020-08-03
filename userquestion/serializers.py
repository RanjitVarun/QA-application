from rest_framework import serializers
from userquestion.models import Question,Answer,Votes,Comments
from usereducationskill.models import Skillset
from login.models import User
from userprofile.models import UserProfile
from userprofile.serializer import ProfileSerializer

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:        
        model = Question 
        fields="__all__"
    
class CommentSerializer(serializers.ModelSerializer):  
    class Meta:        
        model = Comments    
        fields = "__all__"

class VotesSerializer(serializers.ModelSerializer):  
    class Meta:        
        model = Votes    
        fields = "__all__"

class AnswerSerializer(serializers.ModelSerializer): 
    class Meta:        
        model = Answer     
        fields = "__all__"

class AnswerRelSerializer(serializers.ModelSerializer): 
    comments_relation=CommentSerializer(many=True, read_only=True)
    votes_relation =VotesSerializer(many=True, read_only=True)
    class Meta:        
        model = Answer     
        fields = ("id","user","answer","comments_relation","votes_relation")   

class UserRelQuestion(serializers.ModelSerializer):
     profile=ProfileSerializer(read_only=True)
     question_user=QuestionSerializer(many=True, read_only=True)
     answer_user=AnswerRelSerializer(many=True, read_only=True)
     class Meta:
         model= User
         fields =(
            'id','profile',
            "question_user","answer_user") 

class QuestionInfoSerializer(serializers.ModelSerializer):
   
   answer_relation = AnswerRelSerializer(many=True, read_only=True)
   class Meta:
        fields = (
            'id',
            "question",
            'user',
            "answer_relation",
        )
        model = Question

class SkillRelQuestion(serializers.ModelSerializer):
     question_skill=QuestionInfoSerializer(many=True, read_only=True)
     class Meta:
         model= Skillset
         fields =("mainskill","question_skill")        

         