from __future__ import unicode_literals
from django.db import models

from ginthusiasm.models import Gin, UserProfile


class Wishlist(models.Model):
    gins = models.ManyToManyField(Gin)
    user = models.OneToOneField(UserProfile, primary_key=True, related_name='wishlist')

    def __str__(self):
        return self.user.user.username + "'s wishlist"

    def __unicode__(self):
        return self.user.user.username + "'s wishlist"
