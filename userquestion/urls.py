from django.urls import path
import  userquestion.views as view

urlpatterns = [
     path('',view.QuestionCreateView.as_view()),
     path('comments/',view.CommentCreateView.as_view()),
     path('answer/',view.AnswerCreateView.as_view()),
     path('votes/',view.VotesCreateView.as_view()),
     path('<pk>/',view.QuestionUpdateView.as_view()),
     path('<pk>/delete/',view.QuestionDeleteView.as_view()),
     path('<pk>/answer/',view.AnswerUpdateView.as_view()),
     path('<pk>/deleteanswer/',view.AnswerDeleteView.as_view()),
     path('<pk>/comments/',view.CommentUpdateView.as_view()),
     path('<pk>/deletecomments/',view.CommentDeleteView.as_view()),
     path('<pk>/deletevotes/',view.VoteDeleteView.as_view()),
     path('skill/<pk>/',view.SkillQnDetailsView.as_view()),   #specific list  
]
