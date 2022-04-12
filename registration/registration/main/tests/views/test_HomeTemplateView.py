from django.test import TestCase
from django.urls import reverse


class HomeTemplateView(TestCase):
    def test_get__expect_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'index.html')