from django.shortcuts import render
from django.http import HttpResponse

from .models import Question


def index(request):
    question_list = Question.objects.order_by("id")[:5]
    output = ", ".join([q.question_text for q in question_list])

    return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
