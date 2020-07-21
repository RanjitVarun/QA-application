# from django.db import models
# import login.models as login

# # class UserDetails(models.Model): 
# #     first_name=models.CharField(max_length=20,unique=True) 
# #     last_name=models.CharField(max_length=20) 
# #     DOB=models.DateField()
# #     password=models.CharField(max_length=200) 
# #     gender = models.CharField(max_length=1)

# #     def __str__(self): 
# #       return self.first_name 

# class Email(models.Model):
#      user= models.ForeignKey(login.User, on_delete=models.CASCADE, related_name='email_mul',default=1)
#      email_id=models.EmailField(max_length=20) 
     
#      def __str__(self): 
#        return self.email    

# class Mobile(models.Model):
#      user=models.ForeignKey(login.User, on_delete=models.CASCADE,related_name="mobile_mul",default=1) 
#      mobile=models.CharField(max_length=11) 
     
#      def __str__(self): 
#        return self.mobile  

# # class ResAddress(models.Model):
# #      user_id=models.ForeignKey(UserDetails, on_delete=models.CASCADE,related_name="resaddress") 
# #      line1=models.CharField(max_length=20) 
# #      line2=models.CharField(max_length=20)
# #      line3=models.CharField(max_length=20)
# #      landmark=models.CharField(max_length=20)
# #      state=models.CharField(max_length=20)
# #      pin=models.IntegerField()

# #      def __str__(self): 
# #        return '%s %s' % (self.line1, self.line2)         

# # class OfficeAddress(models.Model):
# #      user_id=models.ForeignKey(UserDetails, on_delete=models.CASCADE,related_name="offaddress") 
# #      line1=models.CharField(max_length=11) 
# #      line2=models.CharField(max_length=11)
# #      line3=models.CharField(max_length=11)
# #      landmark=models.CharField(max_length=11)
# #      state=models.CharField(max_length=11)
# #      pin=models.IntegerField()

# #      def __str__(self): 
# #        return '%s %s' % (self.line1, self.line2) 

# # class Education(models.Model):
# #     degree=models.CharField(max_length=20)

# #     def __str__(self): 
# #        return self.degree  

# # class Course(models.Model):
# #     course=models.CharField(max_length=20)

# #     def __str__(self): 
# #        return self.course 

# # class Board(models.Model):
# #     board=models.CharField(max_length=20)

# #     def __str__(self): 
# #        return self.board             

# # class EducationRelUser(models.Model): 
# #     user_id=models.ForeignKey(UserDetails, on_delete=models.CASCADE,related_name="user_relation")
# #     degree=models.ForeignKey(Education, on_delete=models.CASCADE,related_name="degree_relation") 
# #     course=models.ForeignKey(Course, on_delete=models.CASCADE,related_name="course_relation")
# #     board=models.ForeignKey(Board, on_delete=models.CASCADE,related_name="board_relation")

# #     def __str__(self): 
# #        return '%s %s' % (self.degree, self.course)  

# # class Skillset(models.Model):
# #     mainskill=models.CharField(max_length=20)
# #     subskill=models.IntegerField()
    
# #     def __str__(self): 
# #        return self.mainskill      

# # class skillsetRel(models.Model):
# #     skill_id=models.ForeignKey(Skillset, on_delete=models.CASCADE,related_name="skill") 
# #     user_id=models.ForeignKey(UserDetails, on_delete=models.CASCADE,related_name="user_skill")
    
# #     def __str__(self): 
# #        return '%s %s' % (self.skill_id, self.user_id)        
