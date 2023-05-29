from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView

from .models import Question


class QuestionListView(ListView):
    model = Question


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    return render(request, "lmsbaikal/question_detail.html", {"question": question})
