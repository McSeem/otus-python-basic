from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView

from .models import Question


class FilmBaseView(View):
    model = Question
    fields = '__all__'
    success_url = reverse_lazy('questions:all')


class QuestionListView(ListView):


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    return render(request, "lmsbaikal/question_detail.html", {"question": question})
