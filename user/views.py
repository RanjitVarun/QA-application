from django.shortcuts import render
from rest_framework import generics, serializers, views, exceptions
from .models import UserDetails, Email, Mobile, Board, Course, Education, Skillset, skillsetRel
from .serializers import UserSerializer, BoardSerializer,CourseSerializer, BoardCourseSerializer,SkillSerializer
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_multiple_model.views import ObjectMultipleModelAPIView


class UserListView(generics.ListCreateAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserSerializer
    
class UserDetailsView(generics.RetrieveAPIView):
    queryset=UserDetails.objects.all()
    serializer_class = UserSerializer
    
class UserCreateView(generics.CreateAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserSerializer

class UserUpdateView(generics.UpdateAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserSerializer    

class UserDeleteView(generics.DestroyAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserSerializer   

class BoardCourseView(APIView):
    def get(self, request, *args, **kwargs):
          ser = BoardCourseSerializer({'board': Board.objects.all(),'course':Course.objects.all(),
          'degree':Education.objects.all()})
          return Response(ser.data)  

class SkillsetView(generics.ListCreateAPIView):
    queryset = Skillset.objects.all()
    serializer_class =SkillSerializer
    
# class SkillsetView(APIView):
#     def get(self, request, *args, **kwargs):
#           #ser = SkillSerializer({'skills': Skillset.objects.select_related('subskill')})
#           ser = SkillSerializer({'skills': Skillset.objects.all()})
#           return Response(ser.data) 



# class BoardCourseView(ObjectMultipleModelAPIView):
#     def list(self, request, *args, **kwargs):
#         querylist = [
#         {'queryset': Board.objects.all(), 'serializer_class': BoardSerializer},
#         {'queryset': Course.objects.all(), 'serializer_class': CourseSerializer},
#     ] 
#         return HttpResponse(querylist)
    
      


# class BoardView(generics.ListCreateAPIView):
#     model=Board
#     def get_context_data(self, **kwargs):
#         context = super(BoardView, self).get_context_data(**kwargs)
#         context['board']  = Board.objects.all()
#         return context

# class BoardView(generics.ListAPIView):
#     serializer_class = BoardSerializer

#     def get_queryset(self):
#         return list(itertools.chain(Board.objects.all(), Course.objects.all()))
    # def __init__(self, application):
    #     self.application = application

    # def initialize_request(self, request, *args, **kwargs):
    #     print("inital happeinig")
    #     self.model = getattr(self.application, self.kwargs['strmodel'] )
    #     request = super(viewsets.ModelViewSet, self).initialize_request(request, *args, **kwargs)   
    #     return request
    
    # strmodel = None
    # application = None
    # model = Board
    # lookup_field = 'id'

    # def get_queryset(self):     
    #     return self.model.objects.all()
    
    # def get_serializer_class(self):
    #     class BoardSerializer(serializer.ModelSerializer):
    #         class Meta:
    #             model = self.model
    #     return BoardSerializer

    #  queryset = Board.objects.all(), 
    #  print(queryset)                
    #  serializer_class = UserSerializer     
  


   
    
    