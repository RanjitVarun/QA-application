from django.urls import path
import  qa.views as view

urlpatterns = [
     path('',view.QuestionListView.as_view()),
     path('answer/',view.AnswerListView.as_view()),
     path('comments/',view.CommentListView.as_view()),
     path('votes/',view.VotesListView.as_view()),
     path('qlist/',view.QuestionDetailView.as_view()),
]