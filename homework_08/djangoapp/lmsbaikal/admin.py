from django.contrib import admin

from .models import QuestionAnswers, Question

admin.site.register(Question)
admin.site.register(QuestionAnswers)
