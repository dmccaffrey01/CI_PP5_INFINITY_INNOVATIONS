from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch
from .models import Product, Category, Brand
from django.contrib.auth.models import User


class TestViews(TestCase):
    """ Class to test products views """
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

        self.product = Product.objects.create(
            category=self.category,
            brand=self.brand,
            name='TestProduct1',
            description='test',
            price=123.45,
        )

        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            email='testuser@example.com'
        )

        self.superuser = User.objects.create_superuser(
            username='testadmin',
            password='testpassword',
            email='testadmin@example.com'
        )

        self.products_url = reverse('products')
        self.real_products_url = reverse('real_products')
        self.digital_products_url = reverse('digital_products')
        self.product_detail_url = reverse(
            'product_detail', args=[self.product.id])
        self.add_product_url = reverse('add_product')
        self.edit_product_url = reverse('edit_product', args=[self.product.id])
        self.delete_product_url = reverse(
            'delete_product', args=[self.product.id])

        self.client = Client()

    def tearDown(self):
        self.product.delete()
        self.category.delete()
        self.brand.delete()
        self.user.delete()

    def test_products_view(self):
        """ Test all_products view """
        response = self.client.get(self.products_url, {
            'q': 'test',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

        response = self.client.get(self.products_url, {
            'q': '',
        })
        self.assertEqual(response.status_code, 302)

    def test_real_products_view(self):
        """ Test all_products view """
        response = self.client.get(self.real_products_url, {
            'sort': 'name',
            'direction': 'asc',
            'category': 'test',
            'brand': 'test',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_digital_products_view(self):
        """ Test all_products view """
        response = self.client.get(self.digital_products_url, {
            'sort': 'category',
            'direction': 'desc',
            'category': 'test',
            'brand': 'test',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_product_detail_view(self):
        """ Test product detail view """
        response = self.client.get(self.product_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')
