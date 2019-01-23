from django.db import models
#from .models_d import QuestionAnswerTest

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    question_description = models.TextField(
        null=True, blank=True
    )
    pub_date = models.DateTimeField('Дата публикации')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
