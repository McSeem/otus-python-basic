from django.test import TestCase
from .models import QuestionAnswers, Question


class TestViews(TestCase):
    def setUp(self):
        self.response = self.client.get("/lmsbaikal/")

    def test_page_status_code(self):
        """ Тест страницы со списком вопросов. """
        self.assertEqual(self.response.status_code, 200)

    def test_context(self):
        """ Тест передачи контекста, содержащего список вопросов для страницы списка вопросов. """
        question = Question.objects.create(name="Question 1")
        question_answer1 = QuestionAnswers.objects.create(answer="Answer1", question_id=question.id)

        self.assertEqual(self.response.context["question_list"].first().id, question.id)

    def test_content(self):
        """ Тест наличия поля 'course_module_id' на форме добавления нового вопроса. """
        response = self.client.get("/lmsbaikal/question-add/")
        course_module_id_element = '<label for="id_course_module_id">Course module id:</label>'

        self.assertIn(course_module_id_element, response.content.decode(encoding="utf-8"))
        self.assertIn(course_module_id_element.encode(encoding="utf-8"), response.content)
