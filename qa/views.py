from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, serializers, views, exceptions
from django.http import HttpResponse
from rest_framework.response import Response
import qa.models as model
import user.models as usermodels
import qa.serializers as serializer

class QuestionListView(generics.ListCreateAPIView):
    queryset = model.Question.objects.all()
    serializer_class = serializer.QuestionSerializer

class QuestionDeleteView(generics.DestroyAPIView):
    queryset = model.Question.objects.all()
    serializer_class = serializer.QuestionSerializer    

class QuestionDetailView(generics.ListCreateAPIView):
    queryset = model.Question.objects.all()
    serializer_class = serializer.QuestionInfoSerializer

class AnswerListView(generics.ListCreateAPIView):
    queryset = model.Answer.objects.all()
    serializer_class = serializer.AnswerSerializer

class AnswerDeleteView(generics.DestroyAPIView):
    queryset =  model.Answer.objects.all()
    serializer_class =serializer.AnswerSerializer   

class CommentListView(generics.ListCreateAPIView):
    queryset = model.Comments.objects.all()
    serializer_class = serializer.CommentSerializer

class CommentDeleteView(generics.DestroyAPIView):
    queryset =  model.Comments.objects.all()
    serializer_class =serializer.CommentSerializer

class VotesListView(generics.ListCreateAPIView):
    queryset = model.Votes.objects.all()
    serializer_class = serializer.VotesSerializer

class VoteDeleteView(generics.DestroyAPIView):
    queryset =  model.Votes.objects.all()
    serializer_class =serializer.VotesSerializer

class UserQnListView(generics.ListCreateAPIView):
    queryset = usermodels.UserDetails.objects.all()
    serializer_class = serializer.UserRelQuestion

class SkillQnListView(generics.ListCreateAPIView):
    queryset = usermodels.Skillset.objects.all()
    serializer_class = serializer.SkillRelQuestion

class SkillQnDetailsView(generics.RetrieveAPIView):
    queryset = usermodels.Skillset.objects.all()
    serializer_class = serializer.SkillRelQuestion

def index(request):
    return HttpResponse("QA page")
