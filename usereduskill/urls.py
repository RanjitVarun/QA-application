from django.urls import path
import usereduskill.views as views

urlpatterns = [
   path('education/',views.BoardCourseView.as_view()),
   path('addskills/',views.SkillsetCreateView.as_view()),
   path('skills/',views.SkillsetView.as_view()), 
]

