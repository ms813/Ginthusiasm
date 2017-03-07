from django.test import TestCase
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from ginthusiasm.models import UserProfile

class UserTestCase(TestCase):
    def setUp(self):
        user1 = User.objects.create(username="jsmith")
        user1.first_name = "John"
        user1.last_name = "Smith"
        user1.email = "test@test.com"
        user1.password = make_password("jsmith123")

        user1.save()

        profile = UserProfile(user=user1, user_type=UserProfile.BASIC)
        profile.save()


    def test_user_exists(self):
        user = User.objects.get(username="jsmith")
        self.assertIsNotNone(user, "User not null")
        profile = user.userprofile
        self.assertIsNotNone(profile, "Profile not null")

    def test_user_has_wishlist(self):
        wishlist = User.objects.get(username="jsmith").userprofile.wishlist
        self.assertIsNotNone(wishlist, "Has wishlist")
