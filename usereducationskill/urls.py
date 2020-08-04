from django.urls import path
import usereducationskill.views as views


urlpatterns = [
   path('',views.BoardCourseView.as_view()), #list education allong with board,course,degree
   path('usereducation/',views.UserEducationView.as_view()), # list of education for related user
   path('skills/',views.SkillsetView.as_view()), 
   path('userskills/',views.SkillUserView.as_view()),
   #path('adduserskills/',views.SkillsetCreateView.as_view()), 
   path('<pk>/deleteuserskills/',views.SkillsetDeleteView.as_view()),
]

