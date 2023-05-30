from django.test import TestCase

from .models import Question


class TestQuestion(TestCase):
    def setUp(self):
        self.question = Question.objects.create(name="Question 1")

    def test_init(self):
        self.assertEqual(self.question.name, "Question 1")

    def test_str(self):
        self.assertEqual(str(self.question), "Question 1")

    def test_question_tags_count(self):
        tags = ["tag1", "tag2", "tag3"]

        for tag in tags:
            self.question.tags.append(tag)

        self.question.save()

        self.assertEqual(self.question.get_tags_count(), 3)
