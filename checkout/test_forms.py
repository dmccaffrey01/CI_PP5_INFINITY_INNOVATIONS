from django.test import TestCase
from .forms import OrderForm


class TestCheckoutForms(TestCase):
    """
    A class for testing checkout forms
    """

    def test_order_form(self):
        """
        This test tests the order form object
        """
        form = OrderForm({
            'full_name': 'Full Name',
            'email': 'test@gmail.com',
            'phone_number': '123456',
            'postcode': '12345',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality',
            'country': 'US',
        })

        self.assertTrue(form.is_valid())

    def test_invalid_order_form(self):
        """
        This test tests the order form object
        """
        form = OrderForm({})

        self.assertFalse(form.is_valid())



