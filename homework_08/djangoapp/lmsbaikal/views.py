from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView, CreateView, UpdateView

from .models import Question


class QuestionListView(ListView):
    model = Question


class QuestionDetailView(DetailView):
    model = Question


class QuestionNewView(CreateView):
    model = Question
    fields = "__all__"
    success_url = "/lmsbaikal/"


class QuestionUpdateView(UpdateView):
    model = Question
    fields = "__all__"
    success_url = "/lmsbaikal/"
