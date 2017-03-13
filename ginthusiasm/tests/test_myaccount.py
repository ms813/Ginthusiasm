from django.test import TestCase, Client
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from ginthusiasm.models import UserProfile, Distillery


class TestMyAccount(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create(username="jsmith")
        self.user.first_name = "John"
        self.user.last_name = "Smith"
        self.user.email = "test@test.com"
        self.user.password = make_password("jsmith123")

        # Create a test user profile
        self.user.userprofile = UserProfile(user=self.user, user_type=UserProfile.BASIC)
        self.user.userprofile.save()
        self.user.save()

        self.client = Client()

    def test_myaccount_page_basic(self):
        self.client.login(username="jsmith", password="jsmith123")
        response = self.client.get(reverse('myaccount'))

        # profile picture
        self.assertContains(response, '<img src="/media/profile_images/',
                            msg_prefix="My account contains profile image")

        # wishlist button
        self.assertContains(response,
                            '<a class="ginthusiasm-button" href="/wishlist/jsmith/"><span>Wishlist</span></a>',
                            msg_prefix="My account contains wishlist link")

        # My Reviews button
        self.assertContains(response,
                            '<a class="ginthusiasm-button" href="/review/jsmith/"><span>My reviews</span></a>',
                            msg_prefix="My account contains my reviews link")

        # log out button
        self.assertContains(response,
                            '<a class="ginthusiasm-button" href="/logout/"><span>Log Out</span></a>',
                            msg_prefix="My account contains logout button")

    def test_myaccount_page_expert(self):
        # upgrade test user to expert
        self.user.userprofile.user_type = UserProfile.EXPERT
        self.user.userprofile.save()

        self.client.login(username="jsmith", password="jsmith123")
        response = self.client.get(reverse('myaccount'))
        self.assertContains(response,
                            '<a class="ginthusiasm-button" href="/article/jsmith/"><span>My articles</span></a>',
                            msg_prefix="My Account for Expert users contains link to My Articles")

    def test_myaccount_page_distilleryowner(self):
        # upgrade test user to distillery owner
        self.user.userprofile.user_type = UserProfile.DISTILLERY_OWNER
        self.user.userprofile.save()

        distillery = Distillery(name="TestDistillery")
        distillery.owner = self.user.userprofile
        distillery.lat = 0
        distillery.long = 0
        distillery.save()

        self.client.login(username="jsmith", password="jsmith123")
        response = self.client.get(reverse('myaccount'))

        self.assertContains(response,
                            '<a href="/distillery/testdistillery/add-gin/" id="add-gin-btn"',
                            msg_prefix="My Account for distillery owners contains link to add gin to their distillery")
