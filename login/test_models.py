from django.test import TestCase
from login.models import User

class UserModelTest(TestCase):

    def setUp(self):
        User.objects.create(email="email1@gmail.com", password='email1')

    def test_email_max_length(self):
        user = User.objects.get(email="email1@gmail.com")
        max_length = user._meta.get_field('email').max_length
        self.assertEquals(max_length, 255)

    def test_normal_user(self):
        user = User.objects.get(email="email1@gmail.com")
        value=user.is_staff
        self.assertEquals(value,False)

