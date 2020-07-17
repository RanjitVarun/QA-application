from django.urls import path
import user.views as views

urlpatterns = [
   path('',views.UserListView.as_view()),
   path('login/',views.UserLoginView.as_view()),
   path('education/',views.BoardCourseView.as_view()),
   path('addemail/',views.EmailCreateView.as_view()),
   path('addmobile/',views.MobileCreateView.as_view()),
   path('addskills/',views.SkillsetCreateView.as_view()),
   path('addofficeaddress/',views.OffAddressCreateView.as_view()),
   path('<pk>/updateoffaddress/',views.OffAddressUpdateView.as_view()),
   path('<pk>/deleteofficeaddress/',views.OffAddressDeleteView.as_view()),
   path('addresaddress/',views.ResAddressCreateView.as_view()),
   path('<pk>/updateresaddress/',views.ResAddressUpdateView.as_view()),
   path('<pk>/deleteresaddress/',views.ResAddressDeleteView.as_view()),
   path('<pk>/deleteemail/',views.EmailDeleteView.as_view()),
   path('<pk>/deletemobile/',views.MobileDeleteView.as_view()),
   path('skills/',views.SkillsetView.as_view()),
   path('create/',views.UserCreateView.as_view()),
   path('<pk>/',views.UserDetailsView.as_view()),
   path('<pk>/update/',views.UserUpdateView.as_view()),
   path('<pk>/delete/',views.UserDeleteView.as_view()),
   
]

