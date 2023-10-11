from django.urls import reverse
from django.test import TestCase, Client

from products.models import Product, Category, Brand


class TestViews(TestCase):
    """ Class to test checkout view """

    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
        self.brand = Brand.objects.create(name='Test Brand')
        self.product = Product.objects.create(
            name='Test Product',
            category=self.category,
            brand=self.brand,
            price=9.99
        )
        self.add_to_cart_url = reverse('add_to_cart', args=[self.product.id])
        self.adjust_cart_url = reverse('adjust_cart', args=[self.product.id])
        self.remove_from_cart_url = reverse(
            'remove_from_cart', args=[self.product.id])
        self.redirect_url = reverse('view_cart')

        self.client = Client()

    def tearDown(self):
        self.product.delete()
        self.category.delete()
        self.brand.delete()

    def test_view_cart_view(self):
        response = self.client.get(self.redirect_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart.html')

    def test_add_to_cart_view_a(self):
        response = self.client.post(self.add_to_cart_url, {
            'quantity': 1,
            'redirect_url': self.redirect_url,
            'product_theme': 'original',
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            self.client.session.get(
                'cart'), {'1': {'items_by_theme': {'original': 1}}})

        response = self.client.post(self.add_to_cart_url, {
            'quantity': 1,
            'redirect_url': self.redirect_url,
            'product_theme': 'original',
        })

        self.assertEqual(
            self.client.session.get(
                'cart'), {'1': {'items_by_theme': {'original': 2}}})
        self.assertEqual(response.status_code, 302)

        response = self.client.post(self.add_to_cart_url, {
            'quantity': 1,
            'redirect_url': self.redirect_url,
            'product_theme': 'black',
        })

        self.assertEqual(self.client.session.get('cart'), {'1': {
            'items_by_theme': {
                'original': 2,
                'black': 1,
                }
            }})
        self.assertEqual(response.status_code, 302)

    def test_add_to_cart_view_b(self):

        response = self.client.post(self.add_to_cart_url, {
            'quantity': 1,
            'redirect_url': self.redirect_url,
        })

        self.assertEqual(self.client.session.get('cart'), {'1': 1})
        self.assertEqual(response.status_code, 302)

        response = self.client.post(self.add_to_cart_url, {
            'quantity': 1,
            'redirect_url': self.redirect_url,
        })

        self.assertEqual(self.client.session.get('cart'), {'1': 2})
        self.assertEqual(response.status_code, 302)

    def test_adjust_cart_view_a(self):
        session = self.client.session
        session['cart'] = {'1': {'items_by_theme': {'original': 2}}}
        session.save()

        response = self.client.post(self.adjust_cart_url, {
            'quantity': 1,
            'product_theme': 'original',
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            self.client.session.get(
                'cart'), {'1': {'items_by_theme': {'original': 1}}})

        response = self.client.post(self.adjust_cart_url, {
            'quantity': 0,
            'product_theme': 'original',
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session.get('cart'), {})

    def test_adjust_cart_view_b(self):

        session = self.client.session
        session['cart'] = {'1': 1}
        session.save()

        response = self.client.post(self.adjust_cart_url, {
            'quantity': 1,
        })

        self.assertEqual(self.client.session.get('cart'), {'1': 1})
        self.assertEqual(response.status_code, 302)

        response = self.client.post(self.adjust_cart_url, {
            'quantity': 0,
        })

        self.assertEqual(self.client.session.get('cart'), {})
        self.assertEqual(response.status_code, 302)

    def test_remove_from_cart_view_a(self):

        session = self.client.session
        session['cart'] = {'1': {'items_by_theme': {'original': 1}}}
        session.save()

        response = self.client.post(self.remove_from_cart_url, {
            'product_theme': 'original',
        })

        self.assertEqual(self.client.session.get('cart'), {})
        self.assertEqual(response.status_code, 200)

    def test_remove_from_cart_view_b(self):

        session = self.client.session
        session['cart'] = {'1': 1}
        session.save()

        response = self.client.post(self.remove_from_cart_url)

        self.assertEqual(self.client.session.get('cart'), {})
        self.assertEqual(response.status_code, 200)
