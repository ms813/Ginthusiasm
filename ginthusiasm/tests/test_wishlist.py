from django.test import TestCase, Client
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from ginthusiasm.models import UserProfile, Wishlist, Gin


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

        Wishlist.objects.create(user=self.profile)

    # Check the wishlist has been created
    def test_wishlist_exists(self):
        self.assertIsNotNone(self.user.userprofile.wishlist, "Wishlist exists")

    # Check the wishlist page exists and has 0 gins on it
    def test_wishlist_page_exists(self):
        response = self.client.get(reverse('wishlist', kwargs={'username': 'jsmith'}))
        self.assertContains(response, "This user hasn't added any gins to their wishlist!")

    # Check gins can be added to the wishlist
    def test_wishlist_add_remove(self):
        wishlist = self.user.userprofile.wishlist

        self.assertEqual(len(wishlist.gins.all()), 0, "Wishlist empty")
        gins = [
            Gin.objects.create(name="TestGin1"),
            Gin.objects.create(name="TestGin2"),
            Gin.objects.create(name="TestGin3"),
        ]

        for gin in gins:
            wishlist.gins.add(gin)

        self.assertEqual(len(wishlist.gins.all()), 3)

        wishlist.gins.remove(gins[0])
        self.assertEqual(len(wishlist.gins.all()), 2)

        wishlist.gins.clear()
        self.assertEqual(len(wishlist.gins.all()), 0)