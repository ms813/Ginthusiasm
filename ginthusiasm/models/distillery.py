from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.db import models

"""
Model representing a Distillery

Gins are associated with a single Distillery
"""


class Distillery(models.Model):
    name = models.CharField(max_length=225, unique=True, blank=True)
    address = models.CharField(max_length=225, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)
    long_description = models.TextField(blank=True)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='distilleries', blank=True)
    lat = models.FloatField(blank=True)
    long = models.FloatField(blank=True)

    # *args, **kwargs = a way of specifying that a method/function can take
    # extra parameters depending on future use (e.g. if need to save a Distillery
    # in a specific way with something models.Model provides). *args = arguments, and
    # **kwargs = keyword arguments. E.g. could call save(<extra parameters>)
    # which would then get passed to the save method on the models.Model class. Means
    # do not need to define lots of different save methods.

    # override the save method to automatically set the slug based on the name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        # Get super class of Distillery (models.Model) & call its save method, and
        # pass *args and **kwargs that were passed to this class's save method above.
        super(Distillery, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
