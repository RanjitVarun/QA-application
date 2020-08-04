from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, serializers, views, exceptions
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from login.models import User
from userquestion.models import Question,Answer,Votes,Comments
from userquestion.serializers import (QuestionSerializer,QuestionInfoSerializer,AnswerSerializer,AnswerRelSerializer,
CommentSerializer,VotesSerializer,UserRelQuestion,SkillRelQuestion, CommentRelSerializer,VotesRelSerializer)
from usereducationskill.models import Skillset
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from userprofile.models import UserProfile

#question create,delete,
# class QuestionCreateView(generics.CreateAPIView):
#     serializer_class = QuestionSerializer

class QuestionCreateView(generics.CreateAPIView): 
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    serializer_class = QuestionSerializer

    def post(self, request):
        user = User.objects.get(email=request.user)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        Question.objects.create(
            user=user,
            skill=Skillset.objects.get(mainskill=serializer.validated_data.pop('skill')),
            question=serializer.validated_data.pop('question'),
            name=UserProfile.objects.get(user=user).first_name
        )
        status_code = status.HTTP_201_CREATED
        response = {
                'success': 'true',
                'status code': status_code,
                'message': 'Question Posted successfully',
                }
        return Response(response, status=status_code)


class QuestionUpdateView(generics.UpdateAPIView):
    serializer_class = QuestionSerializer    

class QuestionDeleteView(generics.DestroyAPIView):
    serializer_class = QuestionSerializer    

#answer create,delete,
class AnswerCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    serializer_class = AnswerSerializer

    def post(self, request):
        user = User.objects.get(email=request.user)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        Answer.objects.create(
            user=user,
            question=Question.objects.get(question=serializer.validated_data.pop('question')),
            answer=serializer.validated_data.pop('answer'),
            name=UserProfile.objects.get(user=user).first_name
        )
        status_code = status.HTTP_201_CREATED
        response = {
                'success': 'true',
                'status code': status_code,
                'message': 'Answer Posted successfully',
                }
        return Response(response, status=status_code)


class AnswerUpdateView(generics.UpdateAPIView):
    serializer_class = AnswerSerializer   

class AnswerDeleteView(generics.DestroyAPIView):
    serializer_class =AnswerSerializer  

#comment create,delete,
class CommentCreateView(generics.CreateAPIView):
    serializer_class =CommentRelSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    def post(self, request):
        user = User.objects.get(email=request.user)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        Comments.objects.create(
            user=user,
            answer=Answer.objects.get(answer=serializer.validated_data.pop('answer')),
            comments=serializer.validated_data.pop('comments'),
            name=UserProfile.objects.get(user=user).first_name
        )
        status_code = status.HTTP_201_CREATED
        response = {
                'success': 'true',
                'status code': status_code,
                'message': 'Comment Posted successfully',
                }
        return Response(response, status=status_code)

class CommentUpdateView(generics.UpdateAPIView):
    serializer_class = CommentSerializer

class CommentDeleteView(generics.DestroyAPIView):
    serializer_class =CommentSerializer

#votes create,delete,
class VotesCreateView(generics.CreateAPIView):
    serializer_class = VotesRelSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    def post(self, request):
        user = User.objects.get(email=request.user)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        Votes.objects.create(
            user=user,
            answer=Answer.objects.get(answer=serializer.validated_data.pop('answer')),
            votes=serializer.validated_data.pop('votes')
        )
        status_code = status.HTTP_201_CREATED
        response = {
                'success': 'true',
                'status code': status_code,
                'message': 'Vote Added',
                }
        return Response(response, status=status_code)

class VoteDeleteView(generics.DestroyAPIView):
    serializer_class =VotesSerializer

class SkillQnDetailsView(generics.RetrieveAPIView):
    queryset = Skillset.objects.all()
    serializer_class = SkillRelQuestion    

         
       
