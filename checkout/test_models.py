from django.test import TestCase
from .models import Order, OrderLineItem
from products.models import Product, Brand, Category


class TestCheckoutModels(TestCase):
    """
    A class for testing checkout models
    """
    def setUp(self):
        """
        Create a test product and order
        """

        self.order1 = Order.objects.create(
            full_name='Test Name',
            email='test@gmail.com',
            phone_number='123456789',
            street_address1='Test Address',
            street_address2='Test Address2',
            county='test county',
            country='Ireland',
            town_or_city='Test City',
            order_total = 10,
            real_items_total = 10,
        )
        self.category = Category.objects.create(name='Test Category')
        self.brand = Brand.objects.create(name='Test Brand')
        self.product1 = Product.objects.create(
            name='Test Product',
            category=self.category,
            brand=self.brand,
            price=9.99
        )
        self.orderlineitem1 = OrderLineItem.objects.create(
            order=self.order1,
            product=self.product1,
            quantity=1,
        )


    def tearDown(self):
        """
        Delete test products and orders
        """
        self.order1.delete()

    def test_view_cart_view(self):
        self.order1.update_total()