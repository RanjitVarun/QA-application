
from django.shortcuts import render
from rest_framework import generics, serializers, views, exceptions,status
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
import usereduskill.models as model
import usereduskill.serializers as serializer
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

#skill and skilluserrelation 
class SkillsetCreateView(generics.ListCreateAPIView):
    queryset = model.skillsetRel.objects.all()
    serializer_class = serializer.SkillsetSerializer  

class SkillsetView(generics.ListCreateAPIView):
    queryset = model.Skillset.objects.all()
    serializer_class = serializer.SkillSerializer

class SkillsetDeleteView(generics.DestroyAPIView):
    queryset = model.skillsetRel.objects.all()
    serializer_class = serializer.SkillsetSerializer         

#education, board, course related view

class EducationCreateView(generics.CreateAPIView):
    queryset = model.Education.objects.all()
    serializer_class = serializer.EducationSerializer     

class CourseCreateView(generics.CreateAPIView):
    queryset = model.Course.objects.all()
    serializer_class = serializer.CourseSerializer

class BoardCreateView(generics.CreateAPIView):
    queryset = model.Board.objects.all()
    serializer_class = serializer.BoardSerializer


class BoardCourseView(APIView):
    def get(self, request, *args, **kwargs):
          ser = serializer.BoardCourseSerializer({'board': model.Board.objects.all(),'course':model.Course.objects.all(),
          'degree':model.Education.objects.all()})
          return Response(ser.data)  


class UserEducationView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    def get(self, request):
        try:
            user_rel = model.EducationRelUser.objects.get(user=request.user)
            serialize=serializer.EduRelSerializer(user_rel)
            status_code = status.HTTP_200_OK
            response = {
                'success': 'true',
                'status code': status_code,
                'message': 'User Education fetched successfully',
                'data': [{
                    'address':serialize.data }] }

        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'No Education added for this user',
                'error': str(e)
                }
        return Response(response, status=status_code)
    
          








        



      




  


   
    
    
