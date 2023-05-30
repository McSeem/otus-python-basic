from django.test import TestCase

from .models import Question


class TestQuestion(TestCase):
    def test_str(self):
        question = Question.objects.create(name="Question 1")

        self.assertEqual(question.name, "Question 1")
