from django.urls import path
import login.views as views

urlpatterns = [
   path('signup/',views.UserRegistrationView.as_view()),
   path('signin/',views.UserLoginView.as_view()),

]

