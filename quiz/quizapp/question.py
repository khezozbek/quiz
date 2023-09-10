from django.db import models
from .answer import Answer


class Quiz(models.Model):
    question_of_quiz = models.CharField(max_length=500, blank=False, null=False)
    quiz_answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
