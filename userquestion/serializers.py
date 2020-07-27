from rest_framework import serializers
import userquestion.models as userquestionmodels
import usereduskill.models as usereduskill
import login.models as login
from userprofile.serializer import ProfileSerializer


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:        
        model = userquestionmodels.Question      
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):  
    class Meta:        
        model = userquestionmodels.Comments    
        fields = "__all__"

class VotesSerializer(serializers.ModelSerializer):  
    class Meta:        
        model = userquestionmodels.Votes    
        fields = "__all__"

class AnswerSerializer(serializers.ModelSerializer): 
    class Meta:        
        model = userquestionmodels.Answer     
        fields = "__all__"

class AnswerRelSerializer(serializers.ModelSerializer): 
    comments_relation=CommentSerializer(many=True, read_only=True)
    votes_relation =VotesSerializer(many=True, read_only=True)
    class Meta:        
        model = userquestionmodels.Answer     
        fields = ("id","answer","comments_relation","votes_relation")   

class UserRelQuestion(serializers.ModelSerializer):
     #profile=ProfileSerializer(many=True, read_only=True)
     question_user=QuestionSerializer(many=True, read_only=True)
     answer_user=AnswerRelSerializer(many=True, read_only=True)
     class Meta:
         model= login.User
         fields =(
            'id',
            "question_user","answer_user") 

class QuestionInfoSerializer(serializers.ModelSerializer):
   question_user=UserRelQuestion(many=True, read_only=True) 
   answer_relation = AnswerRelSerializer(many=True, read_only=True)
   class Meta:
        fields = (
            "question",
            "answer_relation",
            "question_user"
        )
        model = userquestionmodels.Question

class SkillRelQuestion(serializers.ModelSerializer):
     question_skill=QuestionInfoSerializer(many=True, read_only=True)
     class Meta:
         model= usereduskill.Skillset
         fields =("mainskill","question_skill")        