from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch


class TestViews(TestCase):
    """ Class to test contact views """
    def setUp(self):
        self.contact_url = reverse('contact')

        self.client = Client()

    def test_contact_view(self):
        response = self.client.get(self.contact_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')

    @patch('django.core.mail.send_mail')
    def test_contact_post_view(self, mock_send_mail):
        response = self.client.post(self.contact_url, {
            'name': 'test',
            'email': 'test@test.com',
            'message': 'test',
        })
        self.assertEqual(response.status_code, 302)