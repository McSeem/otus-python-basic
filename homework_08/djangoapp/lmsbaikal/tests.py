from django.test import TestCase

from .models import Question


class TestQuestion(TestCase):
    def test_init(self):
        question = Question.objects.create(name="Question 1")

        self.assertEqual(question.name, "Question 1")

    def test_str(self):
        question = Question.objects.create(name="Question 1")

        self.assertEqual(str(question), "Question 1")

    def test_question_tags_count(self):
        question = Question.objects.create(name="Question 1")

        tags = ["tag1", "tag2", "tag3"]

        for tag in tags:
            question.tags.append(tag)

        question.save()

        self.assertEqual(question.get_tags_count(), 3)
