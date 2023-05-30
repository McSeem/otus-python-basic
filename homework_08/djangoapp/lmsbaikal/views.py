from django.views.generic import DetailView, ListView, CreateView, UpdateView

from .models import Question, QuestionAnswers


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


class QuestionAnswersAddView(CreateView):
    model = QuestionAnswers
    fields = "__all__"
    success_url = "/lmsbaikal/"
