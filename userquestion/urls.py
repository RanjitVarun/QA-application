from django.urls import path
import  userquestion.views as view

urlpatterns = [
     path('',view.QuestionListView.as_view()),
     path('<pk>/delete/',view.QuestionDeleteView.as_view()),
     path('answer/',view.AnswerListView.as_view()),
     path('<pk>/deleteanswer/',view.AnswerDeleteView.as_view()),
     path('comments/',view.CommentListView.as_view()),
     path('<pk>/deletecomments/',view.CommentDeleteView.as_view()),
     path('votes/',view.VotesListView.as_view()),
     path('<pk>/deletevotes/',view.VoteDeleteView.as_view()),
     path('userqlist/',view.UserQnListView.as_view()),
     path('skillqlist/',view.SkillQnListView.as_view()),
     path('<pk>/skillqlist/',view.SkillQnDetailsView.as_view()),
     path('qlist/',view.QuestionDetailView.as_view()),  
]