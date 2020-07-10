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

class ResAddress(models.Model):
     user_id=models.ForeignKey(UserDetails, on_delete=models.CASCADE,related_name="resaddress") 
     line1=models.CharField(max_length=11) 
     line2=models.CharField(max_length=11)
     line3=models.CharField(max_length=11)
     landmark=models.CharField(max_length=11)
     state=models.CharField(max_length=11)
     pin=models.IntegerField()

     def __str__(self): 
       return "Residential Address Added"          

class OfficeAddress(models.Model):
     user_id=models.ForeignKey(UserDetails, on_delete=models.CASCADE,related_name="offaddress") 
     line1=models.CharField(max_length=11) 
     line2=models.CharField(max_length=11)
     line3=models.CharField(max_length=11)
     landmark=models.CharField(max_length=11)
     state=models.CharField(max_length=11)
     pin=models.IntegerField()

     def __str__(self): 
       return "Office Address Added"

class Education(models.Model):
    degree=models.CharField(max_length=10)

    def __str__(self): 
       return self.degree  

class Course(models.Model):
    degree=models.ForeignKey(Education, on_delete=models.CASCADE,related_name="course") 
    course=models.CharField(max_length=50)

    def __str__(self): 
       return self.course 

class Board(models.Model):
    board=models.CharField(max_length=50)

    def __str__(self): 
       return self.board             

class EducationRelUser(models.Model):
    user_id=models.ForeignKey(UserDetails, on_delete=models.CASCADE,related_name="user_relation") 
    degree=models.ForeignKey(Education, on_delete=models.CASCADE,related_name="degree_relation") 
    course=models.ForeignKey(Course, on_delete=models.CASCADE,related_name="course_relation")
    board=models.ForeignKey(Board, on_delete=models.CASCADE,related_name="board_relation")

    def __str__(self): 
       return "Educational details Updated"       