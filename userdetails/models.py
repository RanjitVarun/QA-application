from django.db import models
import login.models as login
import userprofile.models as userprofile
from django.core.validators import MinValueValidator
from phone_field import PhoneField

class Email(models.Model):
     user= models.ForeignKey(login.User, on_delete=models.CASCADE, related_name='emails')
     email=models.EmailField(max_length=20) 
     
     def __str__(self): 
       return self.email  

     class Meta:
        db_table = "email"    

class Mobile(models.Model):
     user=models.ForeignKey(login.User, on_delete=models.CASCADE,related_name="mobiles") 
     mobile = PhoneField(blank=True, max_length=12)
     
     def __str__(self): 
       return self.mobile  

     class Meta:
        db_table = "mobile"  

class ResAddress(models.Model):
     user=models.OneToOneField(login.User, on_delete=models.CASCADE,related_name="resaddress") 
     line1=models.CharField(max_length=50) 
     line2=models.CharField(max_length=50)
     line3=models.CharField(max_length=50)
     landmark=models.CharField(max_length=20)
     state=models.CharField(max_length=20)
     pin=models.PositiveIntegerField(null=False, blank=False)

     def __str__(self): 
       return '%s %s' % (self.line1, self.line2)  

     class Meta:
        db_table = "resaddress"         

class OfficeAddress(models.Model):
     user=models.OneToOneField(login.User, on_delete=models.CASCADE,related_name="offaddress") 
     line1=models.CharField(max_length=50) 
     line2=models.CharField(max_length=50)
     line3=models.CharField(max_length=50)
     landmark=models.CharField(max_length=50)
     state=models.CharField(max_length=50)
     pin=models.PositiveIntegerField(null=False, blank=False)

     def __str__(self): 
       return '%s %s' % (self.line1, self.line2)

     class Meta:
        db_table = "offaddress"   
