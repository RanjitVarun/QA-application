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

class QuestionDetailView(generics.ListCreateAPIView):
    queryset = usermodels.UserDetails.objects.all()
    serializer_class = serializer.QuestionInfoSerializer

class AnswerListView(generics.ListCreateAPIView):
    queryset = model.Answer.objects.all()
    serializer_class = serializer.AnswerSerializer

class CommentListView(generics.ListCreateAPIView):
    queryset = model.Comments.objects.all()
    serializer_class = serializer.CommentSerializer

class VotesListView(generics.ListCreateAPIView):
    queryset = model.Votes.objects.all()
    serializer_class = serializer.VotesSerializer

   

def index(request):
    return HttpResponse("QA page")
