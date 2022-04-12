from django.test import TestCase
from django.urls import reverse


class AboutPageTemplateViewTest(TestCase):

    def test_get__expect_correct_template(self):
        response = self.client.get(reverse('about us page'))
        self.assertTemplateUsed(response, 'main/about-us-page.html')