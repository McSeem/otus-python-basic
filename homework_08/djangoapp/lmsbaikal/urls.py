from django.contrib import admin
from django.urls import path
from .views import QuestionListView

from . import views


urlpatterns = [
    path("", QuestionListView.as_view(), name="all"),
    path("<int:question_id>/", views.detail, name="detail")
]
