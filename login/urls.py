from django.urls import path
import login.views as views

urlpatterns = [
   path('signup/',views.UserRegistrationView.as_view()),
   path('signin/',views.UserLoginView.as_view()),
   path('signout/',views.UserLogoutView.as_view()),
   path('forgotpassword/',views.ForgotPassword.as_view()),
]

