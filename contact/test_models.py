from django.test import TestCase
from .models import ContactMessage
from django.shortcuts import get_object_or_404


class TestContactModels(TestCase):
    """
    A class for testing contact models
    """
    def setUp(self):
        """
        Create a test model object
        """

        self.contact_message = ContactMessage.objects.create(
            name='test',
            email='test@gmail.com',
            message='test',
        )

    def tearDown(self):
        """
        Delete test contact message
        """
        self.contact_message.delete()

    def test_contact_message_model(self):
        """ Test model """
        saved_instance = get_object_or_404(ContactMessage, id=1)
        saved_instance.save()

        self.assertEqual(saved_instance.name, 'test')
        self.assertEqual(str(saved_instance), 'test')
        self.assertEqual(saved_instance.message, 'test')
