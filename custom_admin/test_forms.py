from django.test import TestCase
from .forms import ProductForm, CategoryForm, BrandForm
from products.models import Category, Brand


class TestProductForms(TestCase):
    """
    A class for testing product forms
    """

    def setUp(self):
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

    def test_product_form(self):
        """
        This test tests the product form object
        """

        form = ProductForm({
            'category': self.category.id,
            'brand': self.brand.id,
            'sku': 'test',
            'name': 'TestProduct',
            'description': 'test',
            'has_themes': False,
            'price': '123',
            'rating': '123',
            'image_url': 'http://127.0.0.1:5500/test/',
            'image': 'test.png',
        })

        self.assertTrue(form.is_valid())

    def test_invalid_product_form(self):
        """
        This test tests the product form object
        """

        form = ProductForm({})

        self.assertFalse(form.is_valid())

    def test_category_form(self):
        """
        This test tests the category form object
        """

        form = CategoryForm({
            'name': 'TestCategory',
            'friendly_name': 'TestCategory',
            'universe': 'real',
        })

        self.assertTrue(form.is_valid())

    def test_brand_form(self):
        """
        This test tests the brand form object
        """

        form = BrandForm({
            'name': 'TestBrand',
            'friendly_name': 'TestBrand',
            'universe': 'real',
        })

        self.assertTrue(form.is_valid())
