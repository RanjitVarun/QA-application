from django.urls import path
import userdetails.views as views


urlpatterns = [
   path('',views.AddUserDetailsView.as_view()),
   path('email/',views.EmailCreateView.as_view()),
   path('mobile/',views.MobileCreateView.as_view()),
   path('<pk>/deleteemail/',views.EmailDeleteView.as_view()),
   path('<pk>/deletemobile/',views.MobileDeleteView.as_view()),
   path('<pk>/updateoffaddress/',views.OffAddressUpdateView.as_view()),
   path('<pk>/updateresaddress/',views.ResAddressUpdateView.as_view()),
   
]

