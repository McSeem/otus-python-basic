from django.contrib import admin
from django.urls import path
from .views import QuestionDetailView, QuestionListView, QuestionNewView, QuestionUpdateView, QuestionAnswersAddView


urlpatterns = [
    path("", QuestionListView.as_view()),
    path("<int:pk>/", QuestionDetailView.as_view()),
    path("question-add/", QuestionNewView.as_view()),
    path("question-edit/<int:pk>/", QuestionUpdateView.as_view()),
    path("question-edit/<int:pk>/answer-add/", QuestionAnswersAddView.as_view())
]
