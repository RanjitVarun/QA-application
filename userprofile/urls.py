from django.urls import path
import userprofile.views as views


urlpatterns = [
   path('',views.UserProfileView.as_view()),
   path('update/',views.UserNameUpdateView.as_view()),
   path('list/',views.UserNameList.as_view()),
]

