from django.db import models
from django.contrib.postgres.fields import ArrayField


class Question(models.Model):
    name = models.CharField(max_length=50)
    question_text = models.CharField(max_length=200)
    course_id = models.IntegerField(default=0)
    course_module_id = models.IntegerField(default=0)
    tags = ArrayField(models.CharField(max_length=50, default=''))
    penalty = models.FloatField(default=1.0)


class QuestionAnswers(models.Model):
    question_id = models.IntegerField(default=0)
    answer = models.CharField(max_length=500)
    answer_format = models.IntegerField(default=0)
    fraction = models.FloatField(default=1.0)
    feedback = models.CharField(max_length=50)
    feedback_format = models.IntegerField(default=0)
