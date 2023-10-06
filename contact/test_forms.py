from django.test import TestCase
from .forms import ContactForm


class TestContactForms(TestCase):
    """
    A class for testing contact forms
    """

    def test_contact_form(self):
        """
        This test tests the contact form object
        """
        form = ContactForm({
            'name': 'test',
            'email': 'test@example.com',
            'message': 'test message',
        })

        self.assertTrue(form.is_valid())
    
    def test_invalid_contact_form(self):
        """
        This test tests the contact form object
        """
        form = ContactForm({})

        self.assertFalse(form.is_valid())
