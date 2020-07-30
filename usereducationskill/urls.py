from django.urls import path
import usereducationskill.views as views


urlpatterns = [
   path('education/',views.BoardCourseView.as_view()), #list education allong with board,course,degree
   path('usereducation/',views.UserEducationView.as_view()), # list of education for related user
   path('addusereducation/',views.AddUserEducationView.as_view()), # add user relation to education
   path('addeducation/',views.EducationCreateView.as_view()),
   path('addcourse/',views.CourseCreateView.as_view()),
   path('addboard/',views.BoardCreateView.as_view()),
   path('skills/',views.SkillsetView.as_view()), 
   path('adduserskills/',views.SkillsetCreateView.as_view()), 
   path('viewuserskills/',views.SkillUserView.as_view()),
   path('<pk>/deleteuserskills/',views.SkillsetDeleteView.as_view()),

]

