from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.db import models



class TasteTag(models.Model):
    name = models.CharField(max_length=32, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(TasteTag, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

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
    distillery = models.ForeignKey('distillery', null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Gin, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
