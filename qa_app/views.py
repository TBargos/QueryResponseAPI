from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from typing import Optional

from .db_utils import get_all_questions, get_question

# Create your views here.


@method_decorator(csrf_exempt, name='dispatch')
class QuestionsView(View):
    def get(self, request: HttpRequest, question_id: Optional[int] = None) -> HttpResponse:
        if question_id is not None:
            questions = [get_question(question_id)]
            show_answers = True
        else:
            questions = get_all_questions()
            show_answers = False

        context = {'questions': questions, 'show_answers': show_answers}
        return render(request, 'qa_app/questions.html', context)
    
    def post(self, request: HttpRequest) -> HttpResponse:
        # TODO продумать случай, если сюда попадёт id
        context = {'answer': 'POST-запрос на question'}
        return render(request, 'qa_app/base.html', context)
    
    def delete(self, request: HttpRequest, question_id: int) -> HttpResponse:
        # TODO продумать случай, если сюда не попадёт id
        context = {'answer': 'DELETE-запрос на question'}
        return render(request, 'qa_app/base.html', context)


@method_decorator(csrf_exempt, name='dispatch')
class AnswersView(View):
    def post(self, request: HttpRequest, question_id: int) -> HttpResponse:
        context = {'answer': f'POST-запрос на answer с id {question_id}'}
        return render(request, 'qa_app/base.html', context)

    def get(self, request: HttpRequest, answer_id: int) -> HttpResponse:
        context = context = {'answer': f'GET-запрос на answer с id {answer_id}'}
        return render(request, 'qa_app/base.html', context)

    def delete(self, request: HttpRequest, answer_id: int) -> HttpResponse:
        context = {'answer': f'DELETE-запрос на answer с id {answer_id}'}
        return render(request, 'qa_app/base.html', context)