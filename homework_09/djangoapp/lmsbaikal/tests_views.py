from django.test import TestCase
from  .models import QuestionAnswers, Question


class TestViews(TestCase):
    def test_page_status_code(self):
        response = self.client.get("/lmsbaikal/")

        self.assertEqual(response.status_code, 200)
