from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    question_list = Question.objects.order_by("id")[:5]

    context = {
        "question_list": question_list,
    }

    return render(request, "lmsbaikal/index.html", context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    return render(request, "lmsbaikal/question_detail.html", {"question": question})
