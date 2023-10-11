from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch
from products.models import Product, Category, Brand
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

        self.custom_admin_url = reverse('custom_admin')
        self.products_url = reverse('products')
        self.real_products_url = reverse('real_products')
        self.digital_products_url = reverse('digital_products')
        self.product_detail_url = reverse(
            'product_detail', args=[self.product.id])
        self.add_product_url = reverse('add_product')
        self.edit_product_url = reverse('edit_product', args=[self.product.id])
        self.delete_product_url = reverse(
            'delete_product', args=[self.product.id])
        self.add_category_url = reverse('add_category')
        self.edit_category_url = reverse(
            'edit_category', args=[self.category.id])
        self.delete_category_url = reverse(
            'delete_category', args=[self.category.id])
        self.add_brand_url = reverse('add_brand')
        self.edit_brand_url = reverse('edit_brand', args=[self.brand.id])
        self.delete_brand_url = reverse('delete_brand', args=[self.brand.id])

        self.client = Client()

    def tearDown(self):
        self.product.delete()
        self.category.delete()
        self.brand.delete()
        self.user.delete()

    def test_fail_custom_admin_view(self):
        """ Test custom admin view """

        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.custom_admin_url)
        self.assertEqual(response.status_code, 302)

    def test_success_custom_admin_view(self):
        """ Test custom admin view """

        self.client.login(username='testadmin', password='testpassword')
        response = self.client.get(self.custom_admin_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'custom_admin/custom_admin.html')

    def test_fail_add_product_view(self):
        """ Test fail add product view """

        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.add_product_url)
        self.assertEqual(response.status_code, 302)

    def test_get_add_product_view(self):
        """ Test get add product view """

        self.client.login(username='testadmin', password='testpassword')
        response = self.client.get(self.add_product_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/add_product.html')

    def test_post_add_product_view(self):
        """ Test post add product view """

        self.client.login(username='testadmin', password='testpassword')

        # fail
        response = self.client.post(self.add_product_url, {})

        # success
        response = self.client.post(self.add_product_url, {
            'category': self.category.id,
            'brand': self.brand.id,
            'sku': 'test',
            'name': 'TestProduct2',
            'description': 'test',
            'has_themes': False,
            'price': '123',
            'rating': '123',
            'image_url': 'http://127.0.0.1:5500/test/',
            'image': 'test.png',
        })
        self.assertEqual(response.status_code, 302)
        new_product = Product.objects.get(id=2)
        self.assertEqual(new_product.name, 'TestProduct2')

    def test_fail_edit_product_view(self):
        """ Test fail edit product view """

        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.edit_product_url)
        self.assertEqual(response.status_code, 302)

    def test_get_edit_product_view(self):
        """ Test get edit product view """

        self.client.login(username='testadmin', password='testpassword')
        response = self.client.get(self.edit_product_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/edit_product.html')

    def test_post_edit_product_view(self):
        """ Test post edit product view """

        self.client.login(username='testadmin', password='testpassword')

        # fail
        response = self.client.post(self.edit_product_url, {})

        # success
        response = self.client.post(self.edit_product_url, {
            'category': self.category.id,
            'brand': self.brand.id,
            'sku': 'test',
            'name': 'TestProduct1',
            'description': 'edit_test',
            'has_themes': False,
            'price': '123',
            'rating': '123',
            'image_url': 'http://127.0.0.1:5500/test/',
            'image': 'test.png',
        })
        self.assertEqual(response.status_code, 302)
        new_product = Product.objects.get(id=1)
        self.assertEqual(new_product.description, 'edit_test')

    def test_fail_delete_product_view(self):
        """ Test fail delete product view """

        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.delete_product_url)
        self.assertEqual(response.status_code, 302)

    def test_get_delete_product_view(self):
        """ Test get delete product view """

        self.client.login(username='testadmin', password='testpassword')
        response = self.client.get(self.delete_product_url)
        self.assertEqual(response.status_code, 302)
        deleted_product = Product.objects.filter(id=1).exists()
        self.assertEqual(deleted_product, False)

    def test_fail_add_category_view(self):
        """ Test fail add category view """

        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.add_category_url)
        self.assertEqual(response.status_code, 302)

    def test_get_add_category_view(self):
        """ Test get add category view """

        self.client.login(username='testadmin', password='testpassword')
        response = self.client.get(self.add_category_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'categories/add_category.html')

    def test_post_add_category_view(self):
        """ Test post add category view """

        self.client.login(username='testadmin', password='testpassword')

        # success
        response = self.client.post(self.add_category_url, {
            'name': 'Test Category 2',
            'friendly_name': 'Test Category 2',
            'universe': 'digital',
        })
        self.assertEqual(response.status_code, 302)
        new_category = Category.objects.get(id=2)
        self.assertEqual(new_category.name, 'Test Category 2')

    def test_fail_edit_category_view(self):
        """ Test fail edit category view """

        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.edit_category_url)
        self.assertEqual(response.status_code, 302)

    def test_get_edit_category_view(self):
        """ Test get edit product view """

        self.client.login(username='testadmin', password='testpassword')
        response = self.client.get(self.edit_category_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'categories/edit_category.html')

    def test_post_edit_category_view(self):
        """ Test post edit category view """

        self.client.login(username='testadmin', password='testpassword')

        # success
        response = self.client.post(self.edit_category_url, {
            'name': 'edit_test',
            'friendly_name': 'edit_test',
            'universe': 'digital',
        })
        self.assertEqual(response.status_code, 302)
        new_category = Category.objects.get(id=1)
        self.assertEqual(new_category.name, 'edit_test')

    def test_fail_delete_category_view(self):
        """ Test fail delete category view """

        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.delete_category_url)
        self.assertEqual(response.status_code, 302)

    def test_get_delete_category_view(self):
        """ Test get delete category view """

        self.client.login(username='testadmin', password='testpassword')
        response = self.client.get(self.delete_category_url)
        self.assertEqual(response.status_code, 302)
        deleted_category = Category.objects.filter(id=1).exists()
        self.assertEqual(deleted_category, False)

    def test_fail_add_brand_view(self):
        """ Test fail add brand view """

        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.add_brand_url)
        self.assertEqual(response.status_code, 302)

    def test_get_add_brand_view(self):
        """ Test get add brand view """

        self.client.login(username='testadmin', password='testpassword')
        response = self.client.get(self.add_brand_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'brands/add_brand.html')

    def test_post_add_brand_view(self):
        """ Test post add brand view """

        self.client.login(username='testadmin', password='testpassword')

        # success
        response = self.client.post(self.add_brand_url, {
            'name': 'Test Brand 2',
            'friendly_name': 'Test Brand 2',
            'universe': 'digital',
        })
        self.assertEqual(response.status_code, 302)
        new_brand = Brand.objects.get(id=2)
        self.assertEqual(new_brand.name, 'Test Brand 2')

    def test_fail_edit_brand_view(self):
        """ Test fail edit brand view """

        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.edit_brand_url)
        self.assertEqual(response.status_code, 302)

    def test_get_edit_brand_view(self):
        """ Test get edit brand view """

        self.client.login(username='testadmin', password='testpassword')
        response = self.client.get(self.edit_brand_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'brands/edit_brand.html')

    def test_post_edit_brand_view(self):
        """ Test post edit brand view """

        self.client.login(username='testadmin', password='testpassword')

        # success
        response = self.client.post(self.edit_brand_url, {
            'name': 'edit_test',
            'friendly_name': 'edit_test',
            'universe': 'digital',
        })
        self.assertEqual(response.status_code, 302)
        new_brand = Brand.objects.get(id=1)
        self.assertEqual(new_brand.name, 'edit_test')

    def test_fail_delete_brand_view(self):
        """ Test fail delete brand view """

        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.delete_brand_url)
        self.assertEqual(response.status_code, 302)

    def test_get_delete_brand_view(self):
        """ Test get delete brand view """

        self.client.login(username='testadmin', password='testpassword')
        response = self.client.get(self.delete_brand_url)
        self.assertEqual(response.status_code, 302)
        deleted_brand = Brand.objects.filter(id=1).exists()
        self.assertEqual(deleted_brand, False)
