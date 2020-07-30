from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, serializers, views, exceptions
from django.http import HttpResponse
from rest_framework.response import Response
from login.models import User
from userquestion.models import Question,Answer,Votes,Comments
from userquestion.serializers import (QuestionSerializer,QuestionInfoSerializer,AnswerSerializer,AnswerRelSerializer,
CommentSerializer,VotesSerializer,UserRelQuestion,SkillRelQuestion)
from usereducationskill.models import Skillset

class QuestionListView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDeleteView(generics.DestroyAPIView):
    queryset =Question.objects.all()
    serializer_class = QuestionSerializer    

class QuestionDetailView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionInfoSerializer

class AnswerListView(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class AnswerDeleteView(generics.DestroyAPIView):
    queryset =  Answer.objects.all()
    serializer_class =AnswerSerializer   

class CommentListView(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class =CommentSerializer

class CommentDeleteView(generics.DestroyAPIView):
    queryset =  Comments.objects.all()
    serializer_class =CommentSerializer

class VotesListView(generics.ListCreateAPIView):
    queryset = Votes.objects.all()
    serializer_class = VotesSerializer

class VoteDeleteView(generics.DestroyAPIView):
    queryset =  Votes.objects.all()
    serializer_class =VotesSerializer

class UserQnListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserRelQuestion

class SkillQnListView(generics.ListCreateAPIView):
    queryset = Skillset.objects.all()
    serializer_class = SkillRelQuestion

class SkillQnDetailsView(generics.RetrieveAPIView):
    queryset = Skillset.objects.all()
    serializer_class = SkillRelQuestion

