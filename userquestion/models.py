from django.db import models
from login.models import User
import usereducationskill.models as useredumodels

class Question(models.Model): 
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name="question_user" ) 
    question=models.CharField(max_length=255) 
    skill=models.ForeignKey(useredumodels.Skillset, on_delete=models.CASCADE,related_name="question_skill" ) 
    created = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False) 
  
    def __str__(self): 
      return self.question 

    class Meta:
        db_table = "question"  

class Answer(models.Model): 
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name="answer_user" ) 
    answer=models.CharField(max_length=255) 
    question=models.ForeignKey(Question, on_delete=models.CASCADE,related_name="answer_relation" ) 
    created = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)

  
    def __str__(self): 
      return self.answer

    class Meta:
        db_table = "answer"  

class Comments(models.Model): 
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name="comments" ) 
    Comments=models.CharField(max_length=255) 
    answer=models.ForeignKey(Answer, on_delete=models.CASCADE,related_name="comments_relation" ) 
    created = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)

    def __str__(self): 
      return self.Comments

    class Meta:
        db_table = "comments"  

class Votes(models.Model): 
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name="votes" ) 
    votes=models.BooleanField()
    answer=models.ForeignKey(Answer, on_delete=models.CASCADE,related_name="votes_relation" ) 
    created = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)

    def __str__(self): 
      return self.votes

    class Meta:
        db_table = "votes"  

