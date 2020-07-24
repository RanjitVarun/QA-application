from django.urls import path
import usereduskill.views as views

urlpatterns = [
   path('education/',views.BoardCourseView.as_view()),
   path('addskills/',views.SkillsetCreateView.as_view()),
   path('addeducation/',views.EducationCreateView.as_view()),
   path('addcourse/',views.CourseCreateView.as_view()),
   path('addboard/',views.BoardCreateView.as_view()),
   path('skills/',views.SkillsetView.as_view()), 
]