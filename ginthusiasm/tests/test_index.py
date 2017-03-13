from django.test import TestCase, Client
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from ginthusiasm.models import UserProfile

class IndexTextCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_index_uses_widget_templates(self):
        response = self.client.get("/")

        self.assertTemplateUsed(response, 'ginthusiasm/feature_search_widget.html', "Index uses feature search")
        self.assertTemplateUsed(response, 'ginthusiasm/gin_month_widget.html', "Index uses gin of the month")
        self.assertTemplateUsed(response, 'ginthusiasm/trending_widget.html', "Index uses trending widget")
        self.assertTemplateUsed(response, 'ginthusiasm/collection_highlights_widget.html', "Index uses collection highlights")
