from django.test import TestCase
from .models import Snack
# Create your tests here.


class SnackTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testsnack = Snack.objects.create(title = "test_snack", description="Testing snack")
        testsnack.save()

    def test_snacks_model(self):
        snack = Snack.objects.get(id=1)
        actual_title = snack.title
        self.assertEqual(actual_title, "test_snack")