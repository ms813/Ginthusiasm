from django.test import TestCase, Client, override_settings
from django.urls import reverse


@override_settings(SECURE_SSL_REDIRECT=False)
class TestAbout(TestCase):

    def setUp(self):
        self.client = Client()

    def test_about(self):
        response = self.client.get(reverse('about'))

        self.assertTemplateUsed('ginthusiasm/about.html')
