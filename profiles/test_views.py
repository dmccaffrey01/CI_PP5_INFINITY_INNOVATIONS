from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import UserProfile
from checkout.models import Order, TrackingOrder
from datetime import datetime, timedelta


class TestViews(TestCase):
    """ Class to test profile views """
    def setUp(self):

        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            email='testadmin@example.com'
        )

        self.order = Order.objects.create(
            phone_number='123',
            country='US',
            postcode='123',
            town_or_city='US',
            street_address1='test',
            street_address2='test',
            county='test'
        )

        self.tracking_number = f'tn_{self.order.order_number}'

        self.profile_url = reverse('profile')
        self.order_history_url = reverse('order_history', args=[self.order.order_number])
        self.track_order_url = reverse('track_order', args=[self.order.order_number])
        self.track_order_api_url = reverse('track_order_api', args=[self.tracking_number])

        self.client = Client()

        self.client.login(username='testuser', password='testpassword')

    def tearDown(self):
        self.user.delete()

    def test_get_profile_view(self):
        """ Test profile view """
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_post_profile_view(self):
        """ Test profile post view """
        
        response = self.client.post(self.profile_url, {
            'default_phone_number': '123',
            'default_country': 'US',
            'default_postcode': '123',
            'default_town_or_city': 'test',
            'default_street_address1': 'test',
            'default_street_address2': 'test',
            'default_county': 'test',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

        user_profile_instance = UserProfile.objects.get(user=self.user)

        self.assertEqual(user_profile_instance.default_phone_number, '123')

    def test_order_history_view(self):
        """ Test order history view """
        response = self.client.get(self.order_history_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')

    def test_track_order_view(self):
        """ Test track order view """
        self.order.date = datetime.now() - timedelta(weeks=2)
        self.order.save()
        response = self.client.get(self.track_order_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tracking/tracking_order.html')

    def test_track_order_api(self):
        """ Test track order api """

        self.order.date = datetime.now() - timedelta(weeks=2)
        self.order.save()
        response = self.client.get(self.track_order_api_url)
        self.assertEqual(response.status_code, 200)