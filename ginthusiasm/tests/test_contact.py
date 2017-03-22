from django.test import TestCase, Client, override_settings
from django.urls import reverse
from django.utils.html import escape


@override_settings(SECURE_SSL_REDIRECT=False)
class TestContact(TestCase):

    def setUp(self):
        self.client = Client()

    def test_contact_get(self):
        response = self.client.get(reverse('contact'), follow=True)

        self.assertTemplateUsed('ginthusiasm/contact.html')
        self.assertNotContains(response,
            "We've received your message successfully, thank you. "
            "We will get in touch as soon as possible.")

    def test_contact_post(self):
        data = {
            'name': 'test name',
            'email': 'test@email.com',
            'message': 'test message',
            'date': '2017-03-21',
        }

        response = self.client.post(reverse('contact'), data=data)
        self.assertContains(response, escape(
            "We've received your message successfully, thank you. "
            "We will get in touch as soon as possible."))
