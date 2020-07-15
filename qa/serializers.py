from rest_framework import serializers
import qa.models as qamodels
import user.models as usermodels
import user.serializers as serializer

class QuestionSerializer(serializers.ModelSerializer):    
    class Meta:        
        model = qamodels.Question      
        fields = "__all__"

class AnswerSerializer(serializers.ModelSerializer):    
    class Meta:        
        model = qamodels.Answer     
        fields = "__all__"       

class CommentSerializer(serializers.ModelSerializer):    
    class Meta:        
        model = qamodels.Comments    
        fields = "__all__"

class VotesSerializer(serializers.ModelSerializer):    
    class Meta:        
        model = qamodels.Votes    
        fields = "__all__"

class QuestionInfoSerializer(serializers.ModelSerializer):
   question = QuestionSerializer(many=True, read_only=True)   
   answer = AnswerSerializer(many=True, read_only=True)
   comments =  CommentSerializer(many=True, read_only=True)
   votes = VotesSerializer(many=True, read_only=True)
   class Meta:
        fields = (
            "question",
            "answer",
            "comments",
            "votes"
        )
        model = usermodels.UserDetails