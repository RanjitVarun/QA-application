from django.shortcuts import render
from rest_framework import generics, serializers, views, exceptions,status
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from usereducationskill.models import Board,Course,Education,EducationRelUser,Skillset,skillsetRel
import usereducationskill.serializers as serializer
from usereducationskill.serializers import (SkillsetSerializer,SkillRelSerializer,SkillSerializer,EducationSerializer,CourseSerializer,BoardSerializer,
BoardCourseSerializer,EducationSerializer,EducationRelUser,EduRelSerializer, EduSerializer, SkillUserSerializer)
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from login.models import User

class SkillUserView(generics.ListCreateAPIView): 
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    serializer_class = SkillUserSerializer

    def post(self, request):
        user = User.objects.get(email=request.user)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        skill_details=Skillset.objects.get(mainskill=serializer.validated_data.pop('skill'))
        skillsetRel.objects.create(
            user=user,
            skill=skill_details
            )
        status_code = status.HTTP_201_CREATED
        response = {
                'success': 'true',
                'status code': status_code,
                'message': 'skill added successfully',
                }
        return Response(response, status=status_code)

    def get(self, request):
        try:
            user=User.objects.get(email=request.user)
            serialize=SkillRelSerializer(user)
            status_code = status.HTTP_200_OK
            response = {
                'success': 'true',
                'status code': status_code,
                'message': 'User Education fetched successfully',
                'data':serialize.data }

        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'No Education added for this user',
                'error': str(e)
                }
        return Response(response, status=status_code)

class SkillsetView(generics.ListAPIView):
    queryset = Skillset.objects.all()
    serializer_class = SkillSerializer

class SkillsetDeleteView(generics.DestroyAPIView):
    queryset = skillsetRel.objects.all()
    serializer_class = SkillsetSerializer         

class BoardCourseView(APIView):
    def get(self, request, *args, **kwargs):
          ser = BoardCourseSerializer({'board': Board.objects.all(),'course':Course.objects.all(),
          'degree':Education.objects.all()})
          return Response(ser.data)  


class UserEducationView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    serializer_class = EduSerializer
    def post(self, request):
        user = User.objects.get(email=request.user)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        EducationRelUser.objects.create(
            user=user,
            course=Course.objects.get(course=serializer.validated_data.pop('course')),
            degree=Education.objects.get(degree=serializer.validated_data.pop('degree')),
            board=Board.objects.get(board=serializer.validated_data.pop('board'))
            )
        status_code = status.HTTP_201_CREATED
        response = {
                'success': 'true',
                'status code': status_code,
                'message': 'User Educational details added',
                }
        return Response(response, status=status_code)

    def get(self, request):
        try:
            user_rel = EducationRelUser.objects.get(user=request.user)
            serialize=EduRelSerializer(user_rel)
            status_code = status.HTTP_200_OK
            response = {
                'success': 'true',
                'status code': status_code,
                'message': 'User Education fetched successfully',
                'data':serialize.data }

        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'No Education added for this user',
                'error': str(e)
                }
        return Response(response, status=status_code)
    
          







        



      




  


   
    
    
