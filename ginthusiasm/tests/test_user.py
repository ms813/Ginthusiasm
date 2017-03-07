from django.test import TestCase, Client
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from ginthusiasm.models import UserProfile, Wishlist


class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="jsmith")
        self.user.first_name = "John"
        self.user.last_name = "Smith"
        self.user.email = "test@test.com"
        self.user.password = make_password("jsmith123")

        self.user.save()

        self.profile = UserProfile(user=self.user, user_type=UserProfile.BASIC)
        self.profile.save()

        self.client = Client()

    def test_user_exists(self):
        self.assertIsNotNone(self.user, "User not null")
        profile = self.user.userprofile
        self.assertIsNotNone(profile, "Profile not null")

    def test_user_data(self):
        self.assertEqual(self.user.username, "jsmith", "Username match")
        self.assertEqual(self.user.first_name, "John", "User first_name match")
        self.assertEqual(self.user.last_name, "Smith", "User last_name match")
        self.assertEqual(self.user.email, "test@test.com", "User email match")

    def test_user_login(self):
        response = self.client.post(reverse("login"), {"username" : "jsmith", "password" : "jsmith123"} )
        self.assertRedirects(response, '/my-account/', msg_prefix="Redirect after user login")

    def test_user_logout(self):
        self.client.force_login(self.user)

        user = auth.get_user(self.client)
        self.assertTrue(user.is_authenticated(), "User is authenticated")

        self.client.logout()
        user = auth.get_user(self.client)
        self.assertFalse(user.is_authenticated(), "User not authenticated after log out")






