from django.db import models
import login.models as login


class Education(models.Model):
    degree=models.CharField(max_length=50,)

    def __str__(self): 
       return self.degree  

    class Meta:
        db_table = "education"   

class Course(models.Model):
    course=models.CharField(max_length=50)

    def __str__(self): 
       return self.course 

    class Meta:
        db_table = "course"   

class Board(models.Model):
    board=models.CharField(max_length=50)

    def __str__(self): 
       return self.board 

    class Meta:
        db_table = "board"               

class EducationRelUser(models.Model): 
    user=models.ForeignKey(login.User, on_delete=models.CASCADE,related_name="user_relation")
    degree=models.ForeignKey(Education, on_delete=models.CASCADE,related_name="degree_relation") 
    course=models.ForeignKey(Course, on_delete=models.CASCADE,related_name="course_relation")
    board=models.ForeignKey(Board, on_delete=models.CASCADE,related_name="board_relation")

    def __str__(self): 
       return '%s %s' % (self.degree, self.course)  

    class Meta:
        unique_together = ["user", "degree", "course","board"]
        db_table = "educationreluser"   

class Skillset(models.Model):
    mainskill=models.CharField(max_length=50)
    subskill=models.IntegerField()
    
    def __str__(self): 
       return self.mainskill 

    class Meta:
        db_table = "skillset"        

class skillsetRel(models.Model):
    skill=models.ForeignKey(Skillset, on_delete=models.CASCADE,related_name="skill_set") 
    user=models.ForeignKey(login.User, on_delete=models.CASCADE,related_name="user_skill")
    
    def __str__(self): 
       return '%s %s' % (self.skill, self.user)    

    class Meta:
        unique_together = ["skill","user"]
        db_table = "skillsetrel"       
