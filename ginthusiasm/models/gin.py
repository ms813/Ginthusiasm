from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.db import models
from django.db.models import Avg

"""
A Taste Tag can be associated with a Gin, and can be used for searching
"""


class TasteTag(models.Model):
    name = models.CharField(max_length=32, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    # override the save method to automatically set the slug based on the name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(TasteTag, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


"""
The gin's average rating is updated from ginthusiasm.signals, whenever a Review model is saved
"""


class Gin(models.Model):
    name = models.CharField(max_length=128, unique=True)
    price = models.FloatField(default=0)
    average_rating = models.FloatField(default=0)
    short_description = models.CharField(max_length=1024)
    long_description = models.TextField()
    abv = models.FloatField(default=0)
    taste_tags = models.ManyToManyField(TasteTag, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='gins', blank=True)

    # Gins can be associated with a single distillery
    distillery = models.ForeignKey('distillery', null=True, blank=True)

    # override the save method to automatically set the slug based on the name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Gin, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    # helper function that saves an updated average rating
    def update_average_rating(self):
        rating = self.reviews.aggregate(Avg('rating'))['rating__avg']
        self.average_rating = rating
        self.save()
