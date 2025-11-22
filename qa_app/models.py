import uuid
from django.db import models

# Create your models here.

class Questions(models.Model):
    id = models.BigAutoField(primary_key=True)
    text = models.TextField('текст вопроса')
    created_at = models.DateTimeField('дата публикации')

    class Meta:
        db_table = 'questions'


class Answers(models.Model):
    id = models.BigAutoField(primary_key=True)
    question_id = models.ForeignKey(Questions, on_delete=models.CASCADE)
    user_id = models.UUIDField('идентификатор пользователя', default=uuid.uuid4, editable=False)
    text = models.TextField('текст ответа')
    created_at = models.DateTimeField('дата публикации')

    class Meta:
        db_table = 'answers'