from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

class UserManager(BaseUserManager):
     def create_user(self,first_name,password,email_id): 
        if not email_id:
            raise ValueError("User must have an email")    
        if not password:
            raise ValueError("User must have a password")
        if not first_name:
            raise ValueError("User must have a full name")
        user = self.model(
            email=self.normalize_email(email_id)
        )
        user.first_name = first_name
        user.set_password(password)
        user.admin = is_admin
        user.staff = is_staff
        user.save(using=self._db)
        return user

     def create_superuser(self,first_name,password,email_id): 
        if not email_id:
            raise ValueError("User must have an email")       
        if not password:
         raise ValueError("User must have a password")
        if not first_name:
            raise ValueError("User must have a full name")  
        user = self.model(
            email_id=self.normalize_email(email_id)
        )
        user.first_name = first_name
        user.set_password(password)
        user.admin = True
        user.staff = True
        user.save(using=self._db)
        return user

class UserDetails(AbstractBaseUser): 
    email_id=models.EmailField(max_length=20,default='')
    first_name=models.CharField(max_length=20,unique=True) 
    last_name=models.CharField(max_length=20) 
    DOB=models.DateField()
    gender=models.CharField(max_length=10)
    password=models.CharField(max_length=20) 
    USERNAME_FIELD = 'first_name'
    REQUIRED_FIELDS = ['email_id']
    objects = UserManager()
# GENDER_CHOICES = (
#         ('M', 'Male'),
#         ('F', 'Female'),
#     )

# gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    def __str__(self): 
      return self.first_name 

class Email(models.Model):
     user_id=models.ForeignKey(UserDetails, on_delete=models.CASCADE,related_name="email" ) 
     email=models.EmailField(max_length=20) 
     
     def __str__(self): 
       return self.email    

class Mobile(models.Model):
     user_id=models.ForeignKey(UserDetails, on_delete=models.CASCADE,related_name="mobile") 
     mobile=models.CharField(max_length=11) 
     
     def __str__(self): 
       return self.mobile  

class ResAddress(models.Model):
     user_id=models.ForeignKey(UserDetails, on_delete=models.CASCADE,related_name="resaddress") 
     line1=models.CharField(max_length=20) 
     line2=models.CharField(max_length=20)
     line3=models.CharField(max_length=20)
     landmark=models.CharField(max_length=20)
     state=models.CharField(max_length=20)
     pin=models.IntegerField()

     def __str__(self): 
       return '%s %s' % (self.line1, self.line2)         

class OfficeAddress(models.Model):
     user_id=models.ForeignKey(UserDetails, on_delete=models.CASCADE,related_name="offaddress") 
     line1=models.CharField(max_length=11) 
     line2=models.CharField(max_length=11)
     line3=models.CharField(max_length=11)
     landmark=models.CharField(max_length=11)
     state=models.CharField(max_length=11)
     pin=models.IntegerField()

     def __str__(self): 
       return '%s %s' % (self.line1, self.line2) 

class Education(models.Model):
    degree=models.CharField(max_length=20)

    def __str__(self): 
       return self.degree  

class Course(models.Model):
    degree=models.ForeignKey(Education, on_delete=models.CASCADE,related_name="degree_course") 
    course=models.CharField(max_length=20)

    def __str__(self): 
       return self.course 

class Board(models.Model):
    board=models.CharField(max_length=20)

    def __str__(self): 
       return self.board             

class EducationRelUser(models.Model): 
    user_id=models.ForeignKey(UserDetails, on_delete=models.CASCADE,related_name="user_relation")
    degree=models.ForeignKey(Education, on_delete=models.CASCADE,related_name="degree_relation") 
    course=models.ForeignKey(Course, on_delete=models.CASCADE,related_name="course_relation")
    board=models.ForeignKey(Board, on_delete=models.CASCADE,related_name="board_relation")

    def __str__(self): 
       return '%s %s' % (self.degree, self.course)  

class Skillset(models.Model):
    mainskill=models.CharField(max_length=20)
    subskill=models.IntegerField()
    
    def __str__(self): 
       return self.mainskill      

class skillsetRel(models.Model):
    skill_id=models.ForeignKey(Skillset, on_delete=models.CASCADE,related_name="skill") 
    user_id=models.ForeignKey(UserDetails, on_delete=models.CASCADE,related_name="user_skill")
    
    def __str__(self): 
       return '%s %s' % (self.skill_id, self.user_id)        
