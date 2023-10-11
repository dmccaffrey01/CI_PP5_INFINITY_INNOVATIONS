from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch, Mock


class TestViews(TestCase):
    """ Class to test home views """
    def setUp(self):
        self.home_url = reverse('home')
        self.policy_url = reverse('policy')
        self.reviews_url = reverse('reviews')
        self.add_review_api_url = reverse('add_review_api')

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

    def test_reviews_view(self):
        """ Test reviews view """

        response = self.client.get(self.reviews_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/reviews.html')

    @patch('os.environ.get')
    def test_add_review_api_view(self, mock_api):
        """ Test reviews view """
        mock_api.return_value = 'mock_api'

        data = {
            'message': 'test_message',
        }

        custom_header = {
            'HTTP_REVIEW_POST_API_KEY': 'mock_api',
        }

        response = self.client.post(
            self.add_review_api_url,
            data,
            **custom_header,
        )
        self.assertEqual(response.status_code, 200)

        response = self.client.post(
            self.add_review_api_url,
            data,
        )
        self.assertEqual(response.status_code, 400)

        response = self.client.post(
            self.add_review_api_url,
            {},
            **custom_header,
        )
        self.assertEqual(response.status_code, 400)
