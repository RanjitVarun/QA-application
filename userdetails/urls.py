from django.urls import path
import userdetails.views as views

urlpatterns = [
   path('addemail/',views.EmailCreateView.as_view()),
   path('addmobile/',views.MobileCreateView.as_view()),
   path('<pk>/deleteemail/',views.EmailDeleteView.as_view()),
   path('<pk>/deletemobile/',views.MobileDeleteView.as_view()),
   path('addofficeaddress/',views.OffAddressCreateView.as_view()),
   path('<pk>/updateoffaddress/',views.OffAddressUpdateView.as_view()),
   path('<pk>/deleteofficeaddress/',views.OffAddressDeleteView.as_view()),
   path('addresaddress/',views.ResAddressCreateView.as_view()),
   path('<pk>/updateresaddress/',views.ResAddressUpdateView.as_view()),
   path('<pk>/deleteresaddress/',views.ResAddressDeleteView.as_view()),
]