from django.test import TestCase, Client
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth.models import User
from ginthusiasm.models import UserProfile, Article
from django.contrib.auth.hashers import make_password

class ArticleTestCase(TestCase):
    def setUp(self):
        # Set up a test user
        self.user = User.objects.create(username="testuser")
        self.user.first_name = "Test"
        self.user.last_name = "User"
        self.user.email = "testuser@test.com"
        self.user.password = make_password("testuser123")

        # Create a test user profile
        self.user.userprofile = UserProfile(user=self.user, user_type=UserProfile.EXPERT)
        self.user.userprofile.save()
        self.user.save()

        self.client = Client()

    # Test that the article listing page contains the correct template
    def test_article_widgets(self):
        response = self.client.get(reverse('article_listing'))
        self.assertTemplateUsed(response, 'ginthusiasm/article_listing.html', "Article has listing template")

    # Test that if a user has no articles a message appears
    def test_user_articles(self):
        response = self.client.get(reverse('article_user_listing', kwargs={'user_name': 'testuser'}))
        self.assertContains(response, "No Articles Found")
