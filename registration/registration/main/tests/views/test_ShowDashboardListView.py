from django.test import TestCase
from django.urls import reverse


class ShowDashboardListViewTest(TestCase):
    def test_get__expect_correct_template(self):
        response = self.client.get(reverse('show dashboard'))
        self.assertTemplateUsed(response, 'main/dashboard.html')