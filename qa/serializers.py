# from rest_framework import serializers
# import qa.models as qamodels
# import user.models as usermodels
# import user.serializers as serializer

# class QuestionSerializer(serializers.ModelSerializer):
#     class Meta:        
#         model = qamodels.Question      
#         fields = "__all__"

# class CommentSerializer(serializers.ModelSerializer):  
#     class Meta:        
#         model = qamodels.Comments    
#         fields = "__all__"

# class VotesSerializer(serializers.ModelSerializer):  
#     class Meta:        
#         model = qamodels.Votes    
#         fields = "__all__"

# class AnswerSerializer(serializers.ModelSerializer): 
#     comments_relation=CommentSerializer(many=True, read_only=True)
#     votes_relation =VotesSerializer(many=True, read_only=True)
#     class Meta:        
#         model = qamodels.Answer     
#         fields = ("id","answer","comments_relation","votes_relation")   

# class UserRelQuestion(serializers.ModelSerializer):
#      question_user=QuestionSerializer(many=True, read_only=True)
#      answer_user=AnswerSerializer(many=True, read_only=True)
#      class Meta:
#          model= usermodels.UserDetails
#          fields =(
#             'id',
#             'first_name',"question_user","answer_user") 

# class QuestionInfoSerializer(serializers.ModelSerializer):
#    question_user=UserRelQuestion(many=True, read_only=True) 
#    answer_relation = AnswerSerializer(many=True, read_only=True)
#    class Meta:
#         fields = (
#             "question",
#             "answer_relation",
#             "question_user"
#         )
#         model = qamodels.Question

# class SkillRelQuestion(serializers.ModelSerializer):
#      question_skill=QuestionInfoSerializer(many=True, read_only=True)
#      class Meta:
#          model= usermodels.Skillset
#          fields =("mainskill","question_skill")        