from django.db import models
import user.models as usermodel

class Question(models.Model): 
    user_id=models.ForeignKey(usermodel.UserDetails, on_delete=models.CASCADE,related_name="question" ) 
    question=models.CharField(max_length=255) 
    skill_id=models.ForeignKey(usermodel.Skillset, on_delete=models.CASCADE,related_name="question_skill" ) 
    created = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False) 
  
    def __str__(self): 
      return self.question 

class Answer(models.Model): 
    user_id=models.ForeignKey(usermodel.UserDetails, on_delete=models.CASCADE,related_name="answer" ) 
    answer=models.CharField(max_length=255) 
    question_id=models.ForeignKey(Question, on_delete=models.CASCADE,related_name="answer_relation" ) 
    created = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)

  
    def __str__(self): 
      return self.answer

class Comments(models.Model): 
    user_id=models.ForeignKey(usermodel.UserDetails, on_delete=models.CASCADE,related_name="comments" ) 
    Comments=models.CharField(max_length=255) 
    answer_id=models.ForeignKey(Answer, on_delete=models.CASCADE,related_name="comments_relation" ) 
    created = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)

    def __str__(self): 
      return self.Comments

class Votes(models.Model): 
    user_id=models.ForeignKey(usermodel.UserDetails, on_delete=models.CASCADE,related_name="votes" ) 
    votes=models.BooleanField()
    answer_id=models.ForeignKey(Answer, on_delete=models.CASCADE,related_name="votes_relation" ) 
    created = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)

    def __str__(self): 
      return self.Comments
