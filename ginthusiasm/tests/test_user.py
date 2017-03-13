from django.test import TestCase, Client
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from ginthusiasm.models import UserProfile


class UserTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create(username="jsmith")
        self.user.first_name = "John"
        self.user.last_name = "Smith"
        self.user.email = "test@test.com"
        self.user.password = make_password("jsmith123")

        self.user.save()

        # Create a test user profile
        self.profile = UserProfile(user=self.user, user_type=UserProfile.BASIC)
        self.profile.save()

        self.client = Client()

    # Checks the user has been succcessfully added to the database
    def test_user_exists(self):
        self.assertIsNotNone(self.user, "User not null")
        profile = self.user.userprofile
        self.assertIsNotNone(profile, "Profile not null")

    # Checks the user's data has been saved correctly
    def test_user_data(self):
        self.assertEqual(self.user.username, "jsmith", "Username match")
        self.assertEqual(self.user.first_name, "John", "User first_name match")
        self.assertEqual(self.user.last_name, "Smith", "User last_name match")
        self.assertEqual(self.user.email, "test@test.com", "User email match")

    # Check that the user is able to log in
    def test_user_login(self):
        self.client.login(username="jsmith", password="jsmith123")

        user = auth.get_user(self.client)
        self.assertTrue(user.is_authenticated(), "User is authenticated")

        # Check the page has a log out and my account button
        response = self.client.get("/")
        self.assertContains(response, "My Account", msg_prefix="Logged in user has my account button")
        self.assertContains(response, "Log Out", msg_prefix="Logged in user has log out button")

    # Check that the user is redirected to their 'My Account' page after logging in
    def test_user_redirect_after_login(self):
        response = self.client.post(reverse("login"), {"username": "jsmith", "password": "jsmith123"})
        self.assertRedirects(response, '/my-account/', msg_prefix="Redirect after user login")

    # Check that the user can be logged out
    def test_user_logout(self):
        self.client.force_login(self.user)

        user = auth.get_user(self.client)
        self.assertTrue(user.is_authenticated(), "User is authenticated")
        self.assertFalse(user.is_anonymous(), "User not anonymous after login")

        self.client.logout()
        user = auth.get_user(self.client)
        self.assertFalse(user.is_authenticated(), "User not authenticated after log out")
        self.assertTrue(user.is_anonymous(), "User is anonymous after log out")

        # Check the index page has the login button after logging out
        response = self.client.get('/')
        self.assertContains(response, 'Log In | Sign Up', msg_prefix="Index page has login button after logout")

    # Create a new user by posting to the signup url
    def test_signup(self):
        data = {
            "username": "testuser",
            "password": "password123",
            "first_name": "test",
            "last_name": "user",
            "email": "test@ginthusiasm.com",
        }

        self.client.post(reverse('signup'), data)

        newUser = User.objects.get(username=data["username"])
        self.assertIsNotNone(newUser, "New user signed up")

        # log the new user in and out
        self.client.login(username=data["username"], password=data["password"])
        self.assertTrue(newUser.is_authenticated(), "New user can log in")

        self.client.logout()
        newUser = auth.get_user(self.client)
        self.assertFalse(newUser.is_authenticated(), "New user can log out")
