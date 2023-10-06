from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch


class TestViews(TestCase):
    """ Class to test home views """
    def setUp(self):
        self.home_url = reverse('home')
        self.policy_url = reverse('policy')

        self.client = Client()

    def test_home_view(self):
        """ Test home view """
        
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_policy_view(self):
        """ Test policy view """

        response = self.client.get(self.policy_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'policy/policy.html')
