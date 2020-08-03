from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, serializers, views, exceptions
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from login.models import User
from userquestion.models import Question,Answer,Votes,Comments
from userquestion.serializers import (QuestionSerializer,QuestionInfoSerializer,AnswerSerializer,AnswerRelSerializer,
CommentSerializer,VotesSerializer,UserRelQuestion,SkillRelQuestion)
from usereducationskill.models import Skillset
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

#question create,delete,
class QuestionCreateView(generics.CreateAPIView):
    serializer_class = QuestionSerializer

class QuestionUpdateView(generics.UpdateAPIView):
    serializer_class = QuestionSerializer    

class QuestionDeleteView(generics.DestroyAPIView):
    serializer_class = QuestionSerializer    

#answer create,delete,
class AnswerCreateView(generics.CreateAPIView):
    serializer_class = AnswerSerializer

class AnswerUpdateView(generics.UpdateAPIView):
    serializer_class = AnswerSerializer   

class AnswerDeleteView(generics.DestroyAPIView):
    serializer_class =AnswerSerializer  

#comment create,delete,
class CommentCreateView(generics.CreateAPIView):
    serializer_class =CommentSerializer

class CommentUpdateView(generics.UpdateAPIView):
    serializer_class = CommentSerializer

class CommentDeleteView(generics.DestroyAPIView):
    serializer_class =CommentSerializer

#votes create,delete,
class VotesCreateView(generics.CreateAPIView):
    serializer_class = VotesSerializer

class VoteDeleteView(generics.DestroyAPIView):
    serializer_class =VotesSerializer

#all question list
class QuestionListView(generics.ListAPIView): 
    queryset = Question.objects.all()
    serializer_class = QuestionInfoSerializer

#user specific question,answer,comment,votes
class UserQnListView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserRelQuestion

#skill specific question,answer,comments,votes
class SkillQnDetailsView(generics.RetrieveAPIView):
    queryset = Skillset.objects.all()
    serializer_class = SkillRelQuestion    

         
       
