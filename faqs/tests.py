from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import FAQ
from django.test import TestCase
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'


class FAQAPITests(TestCase):

    def setUp(self):
        self.client = APIClient()
        # Create sample FAQ entries
        FAQ.objects.create(
            question="What is Django?",
            answer="Django is a Python web framework.",
            question_hi="डjango क्या है?",
            question_bn="ডjango কি?"
        )

    def test_fetch_faqs_in_english(self):
        url = reverse('faq-list')  # Assuming 'faq-list' is your URL name
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()
        self.assertIn('What is Django?', [
                      faq['question'] for faq in response_data])

    def test_fetch_faqs_in_hindi(self):
        url = reverse('faq-list') + "?lang=hi"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()
        # Checking if the Hindi translation exists or if it falls back to the English version
        self.assertIn('डjango क्या है?', [faq.get(
            'question_hi', faq['question']) for faq in response_data])

    def test_fetch_faqs_in_bengali(self):
        url = reverse('faq-list') + "?lang=bn"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()
        self.assertIn('ডjango কি?', [faq.get(
            'question_bn', faq['question']) for faq in response_data])
