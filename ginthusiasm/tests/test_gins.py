from django.test import TestCase, Client
from django.shortcuts import reverse
from ginthusiasm.models import Gin, TasteTag, Distillery

class TestGin(TestCase):
    def setUp(self):
        add_gin("Gin1", "Short Description 1", "Long Description 1", "gin/Eden-Mill-Love-Gin.jpg")
        add_gin("Gin2", "Short Description 2", "Long Description 2", "gin/eden-mill-hop-gin.png")
        add_gin("Gin3", "Short Description 3", "Long Description 3", "gin/Eden-Mill-Original-Gin.jpg")

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

def add_gin(name, short_description, long_description, image):
    gin = Gin.objects.get_or_create(name=name)[0]

    gin.short_description = short_description
    gin.long_description = long_description
    gin.image = image

    gin.save()
    return gin
