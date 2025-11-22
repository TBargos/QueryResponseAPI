import uuid
from django.db import models

# Create your models here.

"""Модели:
Question – вопрос:
id: int
text: str (текст вопроса)
created_at: datetime


Answer – ответ на вопрос:
id: int
question_id: int (ссылка на Question)
user_id: str (идентификатор пользователя, например uuid)
text: str (текст ответа)
created_at: datetime
"""


class Question(models.Model):
    id = models.BigAutoField(primary_key=True)
    text = models.TextField('текст вопроса')
    created_at = models.DateTimeField('дата публикации')

    class Meta:
        db_table = 'question'


class Answer(models.Model):
    id = models.BigAutoField(primary_key=True)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_id = models.UUIDField('идентификатор пользователя', default=uuid.uuid4, editable=False)
    text = models.TextField('текст ответа')
    created_at = models.DateTimeField('дата публикации')

    class Meta:
        db_table = 'answer'