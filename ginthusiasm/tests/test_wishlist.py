from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib import auth
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

        self.gins = [
            Gin.objects.create(name="TestGin1"),
            Gin.objects.create(name="TestGin2"),
            Gin.objects.create(name="TestGin3"),
        ]

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

        for gin in self.gins:
            wishlist.gins.add(gin)

        self.assertEqual(len(wishlist.gins.all()), 3)

        for i in range(0, 2):
            self.assertTrue(self.gins[i] in wishlist.gins.all())

        # Check the template contains the names of all the gins
        response = self.client.get(reverse('wishlist', kwargs={'username': 'jsmith'}))
        self.assertContains(response, "TestGin1")
        self.assertContains(response, "TestGin2")
        self.assertContains(response, "TestGin3")
        self.assertTemplateUsed(template_name='ginthusiasm/gin_widget.html', msg_prefix="Wishlist gin_widget used")

        wishlist.gins.remove(self.gins[0])
        self.assertEqual(len(wishlist.gins.all()), 2)

        # Check the template no longer contains TestGin1
        response = self.client.get(reverse('wishlist', kwargs={'username': 'jsmith'}))
        self.assertNotContains(response, "TestGin1")
        self.assertContains(response, "TestGin2")
        self.assertContains(response, "TestGin3")
        self.assertTemplateUsed(template_name='ginthusiasm/gin_widget.html', msg_prefix="Wishlist gin_widget used")

        wishlist.gins.clear()
        self.assertEqual(len(wishlist.gins.all()), 0)

    def test_wishlist_post_addremove(self):
        self.client.login(username="jsmith", password="jsmith123")
        user = auth.get_user(self.client)

        data ={
            'gin_slug' : self.gins[0].slug,
            'user' : user,
        }

        # check wishlist is empty
        user_gins = user.userprofile.wishlist.gins.all()
        self.assertEqual(len(user_gins), 0, "Wishlist empty before post")

        # add a gin by posting to view
        self.client.post(reverse("wishlist_add"), data)

        # check gin just added is now in the wishlist
        user_gins = user.userprofile.wishlist.gins.all()
        self.assertTrue(self.gins[0] in user_gins, "Wishlist add by post")
        self.assertEqual(len(user_gins), 1, "Wishlist post has 1")

        # remove same the gin by post
        self.client.post(reverse("wishlist_add"), data)

        # check the gin has been removed
        user_gins = user.userprofile.wishlist.gins.all()
        self.assertTrue(self.gins[0] not in user_gins, "Wishlist remove by post (not in)")
        self.assertEqual(len(user_gins), 0, "Wishlist remove by post (len)")