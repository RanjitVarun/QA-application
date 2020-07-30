
from django.shortcuts import render
from rest_framework import generics, serializers, views, exceptions,status
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from usereducationskill.models import Board,Course,Education,EducationRelUser,Skillset,skillsetRel
import usereducationskill.serializers as serializer
from usereducationskill.serializers import (SkillsetSerializer,SkillRelSerializer,SkillSerializer,EducationSerializer,CourseSerializer,BoardSerializer,
BoardCourseSerializer,EducationSerializer,EducationRelUser,EduRelSerializer, EduSerializer)
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from login.models import User

#skill and skilluserrelation 

class SkillsetCreateView(generics.CreateAPIView):
    queryset = skillsetRel.objects.all()
    serializer_class = SkillsetSerializer  

class SkillUserView(generics.ListAPIView):
    queryset =skillsetRel.objects.all()
    serializer_class = SkillRelSerializer   

class SkillsetView(generics.ListCreateAPIView):
    queryset = Skillset.objects.all()
    serializer_class = SkillSerializer

class SkillsetDeleteView(generics.DestroyAPIView):
    queryset = skillsetRel.objects.all()
    serializer_class = SkillsetSerializer         

#education, board, course related view

class EducationCreateView(generics.CreateAPIView):
    queryset = Education.objects.all()
    serializer_class =EducationSerializer     

class CourseCreateView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class BoardCreateView(generics.CreateAPIView):
    queryset =Board.objects.all()
    serializer_class = BoardSerializer

class BoardCourseView(APIView):
    def get(self, request, *args, **kwargs):
          ser = BoardCourseSerializer({'board': Board.objects.all(),'course':Course.objects.all(),
          'degree':Education.objects.all()})
          return Response(ser.data)  

class AddUserEducationView(generics.CreateAPIView):
    queryset = EducationRelUser.objects.all()
    serializer_class = EduSerializer

class UserEducationView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

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
    
          








        



      




  


   
    
    
