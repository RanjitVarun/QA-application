from django.urls import path
from login.views import UserRegistrationView,UserLoginView,UserLogoutView,UpdatePassword

urlpatterns = [
   path('',UserRegistrationView.as_view()),
   path('signin/',UserLoginView.as_view()),
   path('signout/',UserLogoutView.as_view()),
   path('updatepassword/',UpdatePassword.as_view()),
]

