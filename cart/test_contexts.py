from decimal import Decimal
from django.test import TestCase
from django.contrib.sessions.middleware import SessionMiddleware
from django.http import HttpRequest
from products.models import Product, Category, Brand
from .contexts import cart_contents

class CartContentsTestCase(TestCase):
    def setUp(self):
        self.category1 = Category.objects.create(name='Test Category 1', universe='real', pk=1)
        self.brand1 = Brand.objects.create(name='Test Brand 1', universe='real')
        self.product1 = Product.objects.create(
            name="Test Product 1",
            price=Decimal('10.00'),
            description='Test Description',
            category=self.category1,
            brand=self.brand1,
        )

        self.category2 = Category.objects.create(name='Test Category 2', universe='digital', pk=2)
        self.brand2 = Brand.objects.create(name='Test Brand 2', universe='digital')
        self.product2 = Product.objects.create(
            name="Test Product 2",
            price=Decimal('10.00'),
            description='Test Description',
            category=self.category2,
            brand=self.brand2,
        )

    def test_cart_contents_a(self):
        request = HttpRequest()
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        request.session['cart'] = {
            '1': 1,
            '2': 1,
        }

        cart_context = cart_contents(request)

        self.assertEqual(cart_context['total'], Decimal('20.00'))
        self.assertEqual(cart_context['product_count'], 2)
        self.assertEqual(cart_context['discounted_total'], Decimal('20.00'))
        self.assertEqual(cart_context['discount_delta'], 180.00)
        self.assertEqual(cart_context['discount_threshold'], 200)
        self.assertEqual(cart_context['discount_percentage'], 10)
        self.assertEqual(round(cart_context['delivery'], 2), round(Decimal(7.99), 2))
        self.assertEqual(round(cart_context['real_items_total'], 2), Decimal('10.00'))
        self.assertEqual(round(cart_context['grand_total'], 2), round(Decimal(27.99),2))
    
    def test_cart_contents_b(self):
        request = HttpRequest()
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        self.product1.price = 150.00
        self.product1.save()

        request.session['cart'] = {
            '1': {'items_by_theme': {'original': 2}},
        }

        cart_context = cart_contents(request)

        self.assertEqual(cart_context['total'], Decimal('300.00'))
        self.assertEqual(cart_context['product_count'], 2)
        self.assertEqual(round(cart_context['discounted_total'], 2), Decimal('270.00'))
        self.assertEqual(cart_context['discount_delta'], 0)
        self.assertEqual(cart_context['discount_threshold'], 200)
        self.assertEqual(cart_context['discount_percentage'], 10)
        self.assertEqual(round(cart_context['delivery'], 2), round(Decimal(7.99), 2))
        self.assertEqual(round(cart_context['real_items_total'], 2), Decimal('300.00'))
        self.assertEqual(round(cart_context['grand_total'], 2), Decimal('277.99'))
        

    def tearDown(self):
        self.product1.delete()
        self.product2.delete()
        self.category1.delete()
        self.category2.delete()
        self.brand1.delete()
        self.brand2.delete()
