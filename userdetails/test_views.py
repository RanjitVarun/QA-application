from django.test import TestCase
from django.urls import reverse

from userdetails.models import Email,Mobile,ResAddress,OfficeAddress

class UserDetailsViewTest(TestCase):
   
    def setUp(self):
       number_of_user = 10
       Email.objects.create(email='testemail@gmail.com',user_id="3123123")
    #    for user_id in range(number_of_user):
    #         Email.objects.create(email='Name'+user_id+'@gmail.com')
    #         Mobile.objects.create(mobile={user_id+'001'})

    def test_view_email(self):
        response = self.client.get('/userdetails/email/')
        self.assertEqual(response.status_code, 200)
           
    