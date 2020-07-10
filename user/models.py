from django.db import models

class UserDetails(models.Model): 
    first_name=models.CharField(max_length=20) 
    last_name=models.CharField(max_length=20) 
    DOB=models.CharField(max_length=15) 
    gender=models.CharField(max_length=10)
    password=models.CharField(max_length=10) 
      
    def __str__(self): 
      return self.first_name 

class Email(models.Model):
     user_id=models.ForeignKey(UserDetails, on_delete=models.CASCADE,related_name="email" ) 
     email=models.EmailField(max_length=254) 
     
     def __str__(self): 
       return self.email    

class Mobile(models.Model):
     user_id=models.ForeignKey(UserDetails, on_delete=models.CASCADE,related_name="mobile") 
     mobile=models.CharField(max_length=11) 
     
     def __str__(self): 
       return self.mobile      