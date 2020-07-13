from django.urls import path

from .views  import UserListView,UserDetailsView, UserCreateView, UserUpdateView, UserDeleteView, BoardCourseView, SkillsetView

urlpatterns = [
   path('',UserListView.as_view()),
   path('education/',BoardCourseView.as_view()),
   path('skills/',SkillsetView.as_view()),
   path('create/',UserCreateView.as_view()),
   path('<pk>/',UserDetailsView.as_view()),
   path('<pk>/update/',UserUpdateView.as_view()),
   path('<pk>/delete/',UserDeleteView.as_view()),
   
 
]

