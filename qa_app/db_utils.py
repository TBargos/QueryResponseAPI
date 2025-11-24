from .models import Questions

from django.db.models.query import QuerySet


def get_all_questions() -> QuerySet[Questions]:
    return Questions.objects.all()


def get_question(question_id: int) -> Questions:
    return Questions.objects.prefetch_related('answers_set').get(pk=question_id)