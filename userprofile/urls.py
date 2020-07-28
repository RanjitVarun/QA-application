from django.urls import path
import userprofile.views as views


urlpatterns = [
   path('',views.UserProfileView.as_view()),
]

