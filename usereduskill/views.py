
from django.shortcuts import render
from rest_framework import generics, serializers, views, exceptions,status
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
import usereduskill.models as model
import usereduskill.serializers as serializer
from django.shortcuts import get_object_or_404
from rest_framework import permissions, status

class SkillsetCreateView(generics.CreateAPIView):
    queryset = model.skillsetRel.objects.all()
    serializer_class = serializer.SkillsetSerializer  

class EducationCreateView(generics.ListCreateAPIView):
    queryset = model.Education.objects.all()
    serializer_class = serializer.EducationSerializer     

class CourseCreateView(generics.ListCreateAPIView):
    queryset = model.Course.objects.all()
    serializer_class = serializer.CourseSerializer

class BoardCreateView(generics.ListCreateAPIView):
    queryset = model.Board.objects.all()
    serializer_class = serializer.BoardSerializer

class SkillsetDeleteView(generics.DestroyAPIView):
    queryset = model.skillsetRel.objects.all()
    serializer_class = serializer.SkillsetSerializer 

class BoardCourseView(APIView):
    def get(self, request, *args, **kwargs):
          ser = serializer.BoardCourseSerializer({'board': model.Board.objects.all(),'course':model.Course.objects.all(),
          'degree':model.Education.objects.all()})
          return Response(ser.data)  

class SkillsetView(generics.ListCreateAPIView):
    queryset = model.Skillset.objects.all()
    serializer_class =serializer.SkillSerializer












        



      




  


   
    
    
