from django.shortcuts import render
from rest_framework import generics, serializers, views, exceptions
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
import user.models as model
import user.serializers as serializer

class UserListView(generics.ListCreateAPIView):
    queryset = model.UserDetails.objects.all()
    serializer_class = serializer.UserSerializer
    
class UserDetailsView(generics.RetrieveAPIView):
    queryset=model.UserDetails.objects.all()
    serializer_class = serializer.UserSerializer
    
class UserCreateView(generics.CreateAPIView):
    queryset = model.UserDetails.objects.all()
    serializer_class = serializer.UserSerializer

class UserUpdateView(generics.UpdateAPIView):
    queryset = model.UserDetails.objects.all()
    serializer_class = serializer.UserSerializer  

class UserDeleteView(generics.DestroyAPIView):
    queryset = model.UserDetails.objects.all()
    serializer_class = serializer.UserSerializer

class EmailCreateView(generics.CreateAPIView):
    queryset = model.Email.objects.all()
    serializer_class = serializer.EmailSerializer

class MobileCreateView(generics.CreateAPIView):
    queryset = model.Mobile.objects.all()
    serializer_class = serializer.MobileSerializer    

class EmailDeleteView(generics.DestroyAPIView):
    queryset = model.Email.objects.all()
    serializer_class = serializer.EmailSerializer

class MobileDeleteView(generics.DestroyAPIView):
    queryset = model.Mobile.objects.all()
    serializer_class = serializer.MobileSerializer 

class SkillsetCreateView(generics.CreateAPIView):
    queryset = model.skillsetRel.objects.all()
    serializer_class = serializer.SkillsetSerializer   

class SkillsetDeleteView(generics.DestroyAPIView):
    queryset = model.skillsetRel.objects.all()
    serializer_class = serializer.SkillsetSerializer 

class MobileDeleteView(generics.DestroyAPIView):
    queryset = model.Mobile.objects.all()
    serializer_class = serializer.MobileSerializer 

class BoardCourseView(APIView):
    def get(self, request, *args, **kwargs):
          ser = serializer.BoardCourseSerializer({'board': model.Board.objects.all(),'course':model.Course.objects.all(),
          'degree':model.Education.objects.all()})
          return Response(ser.data)  

class SkillsetView(generics.ListCreateAPIView):
    queryset = model.Skillset.objects.all()
    serializer_class =serializer.SkillSerializer

class OffAddressCreateView(generics.CreateAPIView):
    queryset = model.OfficeAddress.objects.all()
    serializer_class = serializer.OffAddressSerializer   

class OffAddressUpdateView(generics.UpdateAPIView):
    queryset = model.OfficeAddress.objects.all()
    serializer_class = serializer.OffAddressSerializer

class OffAddressDeleteView(generics.DestroyAPIView):
    queryset = model.OfficeAddress.objects.all()
    serializer_class = serializer.OffAddressSerializer

class ResAddressCreateView(generics.CreateAPIView):
    queryset = model.ResAddress.objects.all()
    serializer_class = serializer.ResAddressSerializer  

class ResAddressUpdateView(generics.UpdateAPIView):
    queryset = model.ResAddress.objects.all()
    serializer_class = serializer.ResAddressSerializer 

class ResAddressDeleteView(generics.DestroyAPIView):
    queryset = model.ResAddress.objects.all()
    serializer_class = serializer.ResAddressSerializer    

# class LoginView(generics.ListCreateAPIView):
#     def post(self, request, *args, **kwargs):s
#         print(request.data)
#         serializer=LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             return Response("valid")
#         else:
#             return Response("invalid")
    #  if serializer.is_valid():
    #     serializer.save()
        #return Response(serializer.data, status=status.HTTP_201_CREATED)
     #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
     
        
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
  


   
    
    