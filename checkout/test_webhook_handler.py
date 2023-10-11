from django.urls import reverse
from django.test import TestCase
from unittest.mock import patch, Mock
from .webhook_handler import StripeWH_Handler

from .models import Order


class TestStripeWHHandler(TestCase):

    def setUp(self):
        self.order = Order.objects.create(
            full_name='test',
            email='test@example.com',
            phone_number='123',
            country='US',
            postcode='123',
            town_or_city='test',
            street_address1='test',
            street_address2='test',
            county='test',
            grand_total=1,
            original_cart='test',
            stripe_pid='test',
        )

        self.mock_request = Mock()

        self.handler = StripeWH_Handler(self.mock_request)

    def tearDown(self):
        self.order.delete()

    def test_handle_event(self):
        response = self.handler.handle_event({'type': 'test'})
        self.assertEqual(response.status_code, 200)

    def test_handle_payment_intent_payment_failed(self):
        response = self.handler.handle_payment_intent_payment_failed(
            {'type': 'test'})
        self.assertEqual(response.status_code, 200)
