from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # see https://docs.djangoproject.com/en/1.10/ref/models/fields/#choices
    BASIC = 'b'
    ADMIN = 'a'
    EXPERT = 'e'
    DISTILLERY_OWNER = 'o'

    USER_TYPE_CHOICES = (
        (BASIC, 'Basic user'),
        (ADMIN, 'Administrator'),
        (EXPERT, 'Expert reviewer'),
        (DISTILLERY_OWNER, 'Distillery Owner'),
    )

    user_type = models.CharField(
        max_length=1,
        choices=USER_TYPE_CHOICES,
        default=BASIC
    )

    profile_image = models.ImageField(
        upload_to='profile_images',
        default="profile_images/judith.jpg"
    )

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username
