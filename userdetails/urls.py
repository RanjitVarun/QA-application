from django.urls import path
import userdetails.views as views


urlpatterns = [
   path('email/',views.EmailCreateView.as_view()),
   path('<pk>/emaillist/',views.EmailList.as_view()),
   path('resaddress/',views.ResAddressView.as_view()),
   path('officeaddress/',views.OfficeAddressView.as_view()),
   path('mobile/',views.MobileCreateView.as_view()),
   path('<pk>/mobilelist/',views.MobileList.as_view()),
   path('<pk>/deleteemail/',views.EmailDeleteView.as_view()),
   path('<pk>/deletemobile/',views.MobileDeleteView.as_view()),
   path('addofficeaddress/',views.OffAddressCreateView.as_view()),
   path('<pk>/updateoffaddress/',views.OffAddressUpdateView.as_view()),
   path('<pk>/deleteofficeaddress/',views.OffAddressDeleteView.as_view()),
   path('addresaddress/',views.ResAddressCreateView.as_view()),
   path('<pk>/updateresaddress/',views.ResAddressUpdateView.as_view()),
   path('<pk>/deleteresaddress/',views.ResAddressDeleteView.as_view()),
]

