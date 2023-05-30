from datetime import datetime

from django.db import models
from django.contrib.postgres.fields import ArrayField


class Question(models.Model):
    name = models.CharField(max_length=50)
    question_text = models.CharField(max_length=200)
    course_id = models.IntegerField(default=0)
    course_module_id = models.IntegerField(default=0)
    tags = ArrayField(models.CharField(max_length=50, default=''), null=True)
    penalty = models.FloatField(default=1.0)
    publication_date = models.DateTimeField("date published", default=datetime.now)
    changed_date = models.DateTimeField("date changed", default=datetime.now)

    def __str__(self):

        return self.name


class QuestionAnswers(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=1)
    answer = models.CharField(max_length=500)
    answer_format = models.IntegerField(default=0)
    fraction = models.FloatField(default=1.0)
    feedback = models.CharField(max_length=50, default=0)
    feedback_format = models.IntegerField(default=0)

    def __str__(self):

        return self.answer
