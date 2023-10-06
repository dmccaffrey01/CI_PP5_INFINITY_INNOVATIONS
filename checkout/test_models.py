from django.test import TestCase
from .models import Order, OrderLineItem
from products.models import Product, Brand, Category
from decimal import Decimal


class TestCheckoutModels(TestCase):
    """
    A class for testing checkout models
    """
    def setUp(self):
        """
        Create a test models objects
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
            delivery_cost=7.99,
            real_items_total=9.99,
            order_total=9.99,
        )
        self.category = Category.objects.create(name='Test Category', universe='real')
        self.brand = Brand.objects.create(name='Test Brand', universe='real')
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

        self.order1.save()


    def tearDown(self):
        """
        Delete test products and orders
        """
        self.order1.delete()
        self.category.delete()
        self.brand.delete()
        self.product1.delete()
        self.orderlineitem1.delete()

    def test_order_model(self):
        self.order1.update_total()
        str_instance = self.order1.order_number
        self.order1.save()

        saved_instance = Order.objects.get(id=1)
        self.assertEqual(saved_instance.real_items_total, round(Decimal(9.99), 2))
        self.assertEqual(saved_instance.grand_total, round(Decimal(17.98), 2))
        self.assertEqual(str(saved_instance), str(str_instance))