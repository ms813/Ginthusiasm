from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify

from ginthusiasm.models import Gin, UserProfile

class Wishlist(models.Model):
    gins = models.ManyToManyField(Gin)
    user = models.OneToOneField(UserProfile)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.user.username)
        super(Wishlist, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.user.username + "'s wishlist"

    def __unicode__(self):
        return self.user.user.username + "'s wishlist"
