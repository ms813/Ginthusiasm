from django.test import TestCase, Client, override_settings
from django.shortcuts import reverse
from ginthusiasm.models import Gin, TasteTag, Distillery, Review, UserProfile
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


@override_settings(SECURE_SSL_REDIRECT=False)
class TestGin(TestCase):
    def setUp(self):
        add_gin("Gin1", "Short Description 1", "Long Description 1", "gin/Eden-Mill-Love-Gin.jpg", 42, 4)
        add_gin("Gin2", "Short Description 2", "Long Description 2", "gin/eden-mill-hop-gin.png", 37.99, 3.6)
        add_gin("Gin3", "Short Description 3", "Long Description 3", "gin/Eden-Mill-Original-Gin.jpg", 35, 3.5)

        self.client = Client()

    def test_adding_gin(self):
        self.assertIsNotNone(Gin.objects.get(name="Gin1"))
        self.assertIsNotNone(Gin.objects.get(name="Gin2"))
        self.assertIsNotNone(Gin.objects.get(name="Gin3"))

    def test_main_gin_page_displays_gin_data(self):
        response = self.client.get(reverse('show_gin', kwargs={'gin_name_slug' : "gin1"}))
        self.assertContains(response, "Gin1")
        self.assertContains(response, "Long Description 1")
        self.assertContains(response, "gin/Eden-Mill-Love-Gin.jpg")

        response = self.client.get(reverse('show_gin', kwargs={'gin_name_slug' : "gin2"}))
        self.assertContains(response, "Gin2")
        self.assertContains(response, "Long Description 2")
        self.assertContains(response, "gin/eden-mill-hop-gin.png")

        response = self.client.get(reverse('show_gin', kwargs={'gin_name_slug' : "gin3"}))
        self.assertContains(response, "Gin3")
        self.assertContains(response, "Long Description 3")
        self.assertContains(response, "gin/Eden-Mill-Original-Gin.jpg")

    def test_gin_search_page_no_parameters(self):
        response = self.client.get(reverse('gin_search_results'))

        self.assertTemplateUsed(template_name='ginthusiasm/gin_search_page.html')
        self.assertTemplateUsed(template_name='ginthusiasm/gin_search_widget.html')
        self.assertTemplateUsed(template_name='ginthusiasm/gin_widget.html')

        self.assertContains(response, "Gin1")
        self.assertContains(response, "Short Description 1")
        self.assertContains(response, "gin/Eden-Mill-Love-Gin.jpg")

        self.assertContains(response, "Gin2")
        self.assertContains(response, "Short Description 2")
        self.assertContains(response, "gin/eden-mill-hop-gin.png")

        self.assertContains(response, "Gin3")
        self.assertContains(response, "Short Description 3")
        self.assertContains(response, "gin/Eden-Mill-Original-Gin.jpg")

    def test_gin_search_page_filter_by_average_rating(self):
        response = self.client.get(reverse('gin_search_results'), {'max_rating' : '5', 'min_rating' : '4'}, follow=True)
        self.assertContains(response, "Gin1")
        self.assertNotContains(response, "Gin2")
        self.assertNotContains(response, "Gin3")

        response = self.client.get(reverse('gin_search_results'), {'max_rating' : '3.9', 'min_rating' : '3'}, follow=True)
        self.assertNotContains(response, "Gin1")
        self.assertContains(response, "Gin2")
        self.assertContains(response, "Gin3")

    def test_gin_search_page_filter_by_price(self):
        response = self.client.get(reverse('gin_search_results'), {'max_price' : '40'}, follow=True)
        self.assertNotContains(response, "Gin1")
        self.assertContains(response, "Gin2")
        self.assertContains(response, "Gin3")

        response = self.client.get(reverse('gin_search_results'), {'min_price' : '40'}, follow=True)
        self.assertContains(response, "Gin1")
        self.assertNotContains(response, "Gin2")
        self.assertNotContains(response, "Gin3")

    def test_gin_search_page_filter_by_keywords(self):
        response = self.client.get(reverse('gin_search_results'), {'keywords' : 'Gin1'}, follow=True)
        self.assertContains(response, "Gin1")
        self.assertNotContains(response, "Gin2")
        self.assertNotContains(response, "Gin3")

    def test_gin_autocomplete_redirect_on_get(self):
        response = self.client.get(reverse('gin_autocomplete'), follow=True)
        self.assertRedirects(response, reverse('gin_search_results'))
        self.assertTemplateUsed('ginthusiasm/gin_search_page.html')

    def test_gin_autocomplete_results(self):
        response = self.client.post(reverse('gin_autocomplete'), data = {'search_text' : 'Gin1'})
        self.assertContains(response, "Gin1")
        self.assertNotContains(response, "Gin2")
        self.assertNotContains(response, "Gin3")

        response = self.client.post(reverse('gin_autocomplete'), data = {'search_text' : 'Gin2'})
        self.assertNotContains(response, "Gin1")
        self.assertContains(response, "Gin2")
        self.assertNotContains(response, "Gin3")

    def test_gin_calculates_average_rating(self):
        gin = add_gin("NewGin", "Short Description", "Long Description", "gin/Eden-Mill-Love-Gin.jpg", 42, 0)

        user = add_user('jsmith', 'John', 'Smith', 'js@test.com', 'jsmith123')
        add_rating(user, gin, 5)
        self.assertEqual(gin.average_rating, 5)

        user = add_user('jdoe', 'Jane', 'Doe', 'jd@test.com', 'jdoe123')
        add_rating(user, gin, 2)
        self.assertEqual(gin.average_rating, 3.5)

        user = add_user('jdoe2', 'John', 'Doe', 'jd2@test.com', 'jdoe432')
        add_rating(user, gin, 2)

        self.assertEqual(gin.average_rating, 3)

    def test_gin_rating(self):
        gin = add_gin("NewGin", "Short Description", "Long Description", "gin/Eden-Mill-Love-Gin.jpg", 42, 0)
        user = add_user('jsmith', 'John', 'Smith', 'js@test.com', 'jsmith123')

        self.client.login(username='jsmith', password='jsmith123')
        response = self.client.post(reverse('rate_gin', kwargs={'gin_name_slug' : "newgin"}), data = {'rating' : '5'})
        self.assertContains(response, 'rated')
        self.assertEqual(gin.reviews.get(user=UserProfile.objects.get(user = user)).rating, 5)



def add_user(username, first_name, last_name, email, password):
    user = User.objects.get_or_create(username = username)[0]
    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    user.password = make_password(password)

    user.save()

    profile = UserProfile(user=user)
    profile.save()

    return user


def add_rating(user, gin, rating):
    review = Review.objects.get_or_create(user=user.userprofile, gin=gin)[0]

    review.rating = rating
    review.save()
    return review



def add_gin(name, short_description, long_description, image, price, average_rating):
    gin = Gin.objects.get_or_create(name=name)[0]

    gin.short_description = short_description
    gin.long_description = long_description
    gin.image = image
    gin.price = price
    gin.average_rating = average_rating

    gin.save()
    return gin
