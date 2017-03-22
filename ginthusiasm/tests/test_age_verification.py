from django.test import TestCase, Client, override_settings
from django.urls import reverse


@override_settings(SECURE_SSL_REDIRECT=False)
class TestAgeVerification(TestCase):

    def setUp(self):
        self.client = Client()

    def test_age_verification(self):
        # verified cookie not set, so age-overlay div should be shown
        response = self.client.get(reverse('index'))
        self.assertContains(response, '<div id="age-overlay"')

        # Set the verified cookie
        self.client.cookies.load({'verified': 'True'})

        # Verified cookie is now set, so age-overlay div should not be shown
        response = self.client.get(reverse('index'))
        self.assertNotContains(response, '<div id="age-overlay"')
