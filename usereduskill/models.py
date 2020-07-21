# from django.db import models
# import login.models as login


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
