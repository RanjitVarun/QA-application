from django.db import models
import uuid
from login.models import User

class UserProfileManager(models.Manager):

    def update_first_name(self,userid,name):
        user=UserProfile.objects.get(user=userid)
        user.first_name=name
        user.save()
        return user

class UserProfile(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=50, unique=False)
    last_name = models.CharField(max_length=50, unique=False)
    phone_number = models.CharField(max_length=10, unique=True, null=False, blank=False)
    age = models.PositiveIntegerField(null=False, blank=False)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    objects=UserProfileManager()

    class Meta:
        db_table = "profile"
