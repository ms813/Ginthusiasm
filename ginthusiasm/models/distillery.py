from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.db import models

class Distillery(models.Model):
    name = models.CharField(max_length=225, unique=True)
    address = models.CharField(max_length=225)
    email = models.EmailField()
    slug = models.SlugField(unique=True)
    img = models.ImageField(upload_to='distilleries')
    lat = models.FloatField(blank=False)
    long = models.FloatField(blank=False)

    # *args, **kwargs = a way of specifying that a method/function can take
    # extra parameters depending on future use (e.g. if need to save a Distillery
    # in a specific way with something models.Model provides). *args = arguments, and
    # **kwargs = keyword arguments. E.g. could call save(<extra parameters>)
    # which would then get passed to the save method on the models.Model class. Means
    # do not need to define lots of different save methods.
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        # Get super class of Distillery (models.Model) & call its save method, and
        # pass *args and **kwargs that were passed to this class's save method above.
        super(Distillery, self).save(*args, **kwargs)

    # 'toString'
    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name