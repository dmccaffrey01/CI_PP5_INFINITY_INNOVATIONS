from django.test import TestCase
from .models import Product, Category, Brand
from django.shortcuts import get_object_or_404


class TestProductModels(TestCase):
    """
    A class for testing contact models
    """
    def setUp(self):
        """
        Create a test model object
        """

        self.category = Category.objects.create(
            name='TestCategory',
            friendly_name='TestCategory',
            universe='real',
        )

        self.brand = Brand.objects.create(
            name='TestBrand',
            friendly_name='TestBrand',
            universe='real',
        )

        self.product = Product.objects.create(
            category=self.category,
            brand=self.brand,
            name='test',
            description='test',
            price=123.45,
        )

    def tearDown(self):
        """
        Delete test product, category and brand
        """
        self.category.delete()
        self.brand.delete()
        self.product.delete()

    def test_category_model(self):
        """ Test models """
        saved_instance = get_object_or_404(Category, id=1)
        saved_instance.save()

        self.assertEqual(saved_instance.name, 'TestCategory')
        self.assertEqual(str(saved_instance), 'TestCategory')

    def test_brand_model(self):
        """ Test models """
        saved_instance = get_object_or_404(Brand, id=1)
        saved_instance.save()

        self.assertEqual(saved_instance.name, 'TestBrand')
        self.assertEqual(str(saved_instance), 'TestBrand')

    def test_product_model(self):
        """ Test models """
        saved_instance = get_object_or_404(Product, id=1)
        saved_instance.save()

        self.assertEqual(saved_instance.name, 'test')
        self.assertEqual(str(saved_instance), 'test')
