from __future__ import unicode_literals
from django.db import models
from user_profile import UserProfile

class Article(models.Model):

    title = models.CharField(max_length=128, unique=True)
    shortDesc = models.TextField(max_length=1000, unique=True)
    content = models.TextField()
    date = models.DateField()
    slug = models.SlugField(max_length=50)
    # Not sure what should be in the foreign key bracket??
    author = models.ForeignKey('UserProfile', related_name='article')

    class Meta:
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title
