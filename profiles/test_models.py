from django.test import TestCase
from .models import UserProfile
from django.contrib.auth.models import User


class TestModels(TestCase):
    """
    A class for testing profile models
    """

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            email='testadmin@example.com'
        )

    def tearDown(self):
        self.user.delete()

    def test_user_profile_model(self):
        """ Test model """

        self.client.login(username='testuser', password='testpassword')

        saved_instance = UserProfile.objects.get(user=self.user)
        saved_instance.default_phone_number = '123'
        saved_instance.save()

        self.assertEqual(saved_instance.default_phone_number, '123')
        self.assertEqual(str(saved_instance), 'testuser')