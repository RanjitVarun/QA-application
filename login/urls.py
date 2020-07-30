from django.urls import path
from login.views import UserRegistrationView,UserLoginView,UserLogoutView,ForgotPassword

urlpatterns = [
   path('signup/',UserRegistrationView.as_view()),
   path('signin/',UserLoginView.as_view()),
   path('signout/',UserLogoutView.as_view()),
   path('forgotpassword/',ForgotPassword.as_view()),
]

