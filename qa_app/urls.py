from django.urls import path

from .views import QuestionsView, AnswersView


app_name = 'qa_app'
urlpatterns = [
    path('questions/', QuestionsView.as_view(), name='all_questions'),
    path('questions/<int:question_id>/', QuestionsView.as_view(), name='questions_by_id'),
    path('questions/<int:question_id>/answers/', AnswersView.as_view(), name='answer_to_question'),
    path('answers/<int:answer_id>/', AnswersView.as_view(), name='answer_by_id'),
    
]