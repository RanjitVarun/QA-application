# from django.shortcuts import render
# from rest_framework import generics, serializers, views, exceptions,status
# from django.http import HttpResponse
# from rest_framework.views import APIView
# from rest_framework.response import Response
# import user.models as model
# import user.serializers as serializer
# from django.shortcuts import get_object_or_404
# from rest_framework import permissions, status

# # class UserListView(generics.ListCreateAPIView):
# #     queryset = model.UserDetails.objects.all()
# #     serializer_class = serializer.UserSerializer
    
# # class UserDetailsView(generics.RetrieveAPIView):
# #     queryset=model.UserDetails.objects.all()
# #     serializer_class = serializer.UserSerializer
    
# # class UserCreateView(generics.CreateAPIView):
# #     queryset = model.UserDetails.objects.all()
# #     serializer_class = serializer.UserSerializer

# # class UserUpdateView(generics.UpdateAPIView):
# #     queryset = model.UserDetails.objects.all()
# #     serializer_class = serializer.UserSerializer  

# # class UserDeleteView(generics.DestroyAPIView):
# #     queryset = model.UserDetails.objects.all()
# #     serializer_class = serializer.UserSerializer

# class EmailCreateView(generics.ListCreateAPIView):
#     queryset = model.Email.objects.all()
#     serializer_class = serializer.EmailSerializer

# class MobileCreateView(generics.ListCreateAPIView):
#     queryset = model.Mobile.objects.all()
#     serializer_class = serializer.MobileSerializer    

# class EmailDeleteView(generics.DestroyAPIView):
#     queryset = model.Email.objects.all()
#     serializer_class = serializer.EmailSerializer

# class MobileDeleteView(generics.DestroyAPIView):
#     queryset = model.Mobile.objects.all()
#     serializer_class = serializer.MobileSerializer 

# # class SkillsetCreateView(generics.CreateAPIView):
# #     queryset = model.skillsetRel.objects.all()
# #     serializer_class = serializer.SkillsetSerializer   

# # class SkillsetDeleteView(generics.DestroyAPIView):
# #     queryset = model.skillsetRel.objects.all()
# #     serializer_class = serializer.SkillsetSerializer 

# # class MobileDeleteView(generics.DestroyAPIView):
# #     queryset = model.Mobile.objects.all()
# #     serializer_class = serializer.MobileSerializer 

# # class BoardCourseView(APIView):
# #     def get(self, request, *args, **kwargs):
# #           ser = serializer.BoardCourseSerializer({'board': model.Board.objects.all(),'course':model.Course.objects.all(),
# #           'degree':model.Education.objects.all()})
# #           return Response(ser.data)  

# # class SkillsetView(generics.ListCreateAPIView):
# #     queryset = model.Skillset.objects.all()
# #     serializer_class =serializer.SkillSerializer

# # class OffAddressCreateView(generics.CreateAPIView):
# #     queryset = model.OfficeAddress.objects.all()
# #     serializer_class = serializer.OffAddressSerializer   

# # class OffAddressUpdateView(generics.UpdateAPIView):
# #     queryset = model.OfficeAddress.objects.all()
# #     serializer_class = serializer.OffAddressSerializer

# # class OffAddressDeleteView(generics.DestroyAPIView):
# #     queryset = model.OfficeAddress.objects.all()
# #     serializer_class = serializer.OffAddressSerializer

# # class ResAddressCreateView(generics.CreateAPIView):
# #     queryset = model.ResAddress.objects.all()
# #     serializer_class = serializer.ResAddressSerializer  

# # class ResAddressUpdateView(generics.UpdateAPIView):
# #     queryset = model.ResAddress.objects.all()
# #     serializer_class = serializer.ResAddressSerializer 

# # class ResAddressDeleteView(generics.DestroyAPIView):
# #     queryset = model.ResAddress.objects.all()
# #     serializer_class = serializer.ResAddressSerializer    









        


# # class BoardCourseView(ObjectMultipleModelAPIView):
# #     def list(self, request, *args, **kwargs):
# #         querylist = [
# #         {'queryset': Board.objects.all(), 'serializer_class': BoardSerializer},
# #         {'queryset': Course.objects.all(), 'serializer_class': CourseSerializer},
# #     ] 
# #         return HttpResponse(querylist)
    
      




  


   
    
    