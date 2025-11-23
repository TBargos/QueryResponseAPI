from django.urls import path

from .views import QuestionsView, AnswersView


app_name = 'qa_app'
urlpatterns = [
    path('questions/', QuestionsView.as_view()),
    path('questions/<int:question_id>/', QuestionsView.as_view()),
    path('questions/<int:question_id>/answers/', AnswersView.as_view()),
    path('answers/<int:answer_id>/', AnswersView.as_view()),
    
]