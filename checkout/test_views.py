from django.urls import reverse
from django.test import TestCase, Client
from unittest.mock import patch
from django.contrib.auth.models import User

from products.models import Product, Category, Brand
from .models import Order


class TestViews(TestCase):
    """
    Class to test the checkout views
    """
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
        self.brand = Brand.objects.create(name='Test Brand')
        self.product = Product.objects.create(
            name='Test Product',
            category=self.category,
            brand=self.brand,
            price=9.99
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

        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            email='testuser@example.com'
        )

        self.cache_checkout_data_url = reverse('cache_checkout_data')
        self.checkout_url = reverse('checkout')
        self.checkout_success_url = reverse(
            'checkout_success', args=[self.order.order_number])

        self.client = Client()

    def tearDown(self):
        self.product.delete()
        self.category.delete()
        self.brand.delete()
        self.user.delete()

    @patch('stripe.PaymentIntent.modify')
    @patch('stripe.api_key', 'test')
    def test_cache_checkout_data_a(self, mock_modify_payment_intent):
        response = self.client.post(self.cache_checkout_data_url, {})
        self.assertEqual(response.status_code, 400)

    @patch('stripe.PaymentIntent.modify')
    @patch('stripe.api_key', 'test')
    def test_cache_checkout_data_b(self, mock_modify_payment_intent):

        response = self.client.post(self.cache_checkout_data_url, {
            'save_info': True,
            'client_secret': 'client_secret',
            })
        self.assertEqual(response.status_code, 200)

    @patch('stripe.PaymentIntent.modify')
    @patch('stripe.api_key', 'test')
    def test_checkout_view_a(self, mock_modify_payment_intent):
        response = self.client.get(self.checkout_url)
        self.assertEqual(response.status_code, 302)

        session = self.client.session
        session['cart'] = {'1': 1}
        session.save()

        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.checkout_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')

    @patch('stripe.PaymentIntent.modify')
    def test_checkout_view_b(self, mock_modify_payment_intent):
        session = self.client.session
        session['cart'] = {'1': 1}
        session.save()

        self.client.login(username='testuser', password='testpassword')

        response = self.client.post(self.checkout_url, {
            'full_name': 'test',
            'email': 'test@gmail.com',
            'phone_number': '12345',
            'country': 'US',
            'postcode': '12345',
            'town_or_city': 'test',
            'street_address1': 'test',
            'street_address2': 'test',
            'county': 'test',
            'client_secret': 'test_secret',
        })
        self.assertEqual(response.status_code, 302)

    @patch('stripe.PaymentIntent.modify')
    def test_checkout_view_c(self, mock_modify_payment_intent):
        session = self.client.session
        session['cart'] = {'1': {'items_by_theme': {'original': 1}}}
        session.save()

        self.client.login(username='testuser', password='testpassword')

        response = self.client.post(self.checkout_url, {
            'full_name': 'test',
            'email': 'test@gmail.com',
            'phone_number': '12345',
            'country': 'US',
            'postcode': '12345',
            'town_or_city': 'test',
            'street_address1': 'test',
            'street_address2': 'test',
            'county': 'test',
            'client_secret': 'test_secret',
        })
        self.assertEqual(response.status_code, 302)

    def test_checkout_success_view(self):
        session = self.client.session
        session['cart'] = {'1': 1}
        session['save_info'] = True
        session.save()

        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.checkout_success_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')
