from django.db import models
import login.models as login
import userprofile.models as userprofile

class Email(models.Model):
     user= models.ForeignKey(login.User, on_delete=models.CASCADE, related_name='emails')
     email=models.EmailField(max_length=20) 
     
     def __str__(self): 
       return self.email  

     class Meta:
        db_table = "email"    

class Mobile(models.Model):
     user=models.ForeignKey(login.User, on_delete=models.CASCADE,related_name="mobiles") 
     mobile=models.CharField(max_length=11) 
     
     def __str__(self): 
       return self.mobile  

     class Meta:
        db_table = "mobile"  

class ResAddress(models.Model):
     user=models.OneToOneField(login.User, on_delete=models.CASCADE,related_name="resaddress") 
     line1=models.CharField(max_length=20) 
     line2=models.CharField(max_length=20)
     line3=models.CharField(max_length=20)
     landmark=models.CharField(max_length=20)
     state=models.CharField(max_length=20)
     pin=models.IntegerField()

     def __str__(self): 
       return '%s %s' % (self.line1, self.line2)  

     class Meta:
        db_table = "resaddress"         

class OfficeAddress(models.Model):
     user=models.OneToOneField(login.User, on_delete=models.CASCADE,related_name="offaddress") 
     line1=models.CharField(max_length=11) 
     line2=models.CharField(max_length=11)
     line3=models.CharField(max_length=11)
     landmark=models.CharField(max_length=11)
     state=models.CharField(max_length=11)
     pin=models.IntegerField()

     def __str__(self): 
       return '%s %s' % (self.line1, self.line2)

     class Meta:
        db_table = "offaddress"   
