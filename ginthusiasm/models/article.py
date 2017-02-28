from __future__ import unicode_literals
from django.db import models
from user_profile import UserProfile
from django.template.defaultfilters import slugify

class Article(models.Model):

    title = models.CharField(max_length=128, unique=True)
    shortDesc = models.TextField(max_length=1000, unique=True)
    content = models.TextField(max_length=1000)
    date = models.DateField()
    slug = models.SlugField(max_length=50,unique=True)
    author = models.ForeignKey('UserProfile', related_name='article')
    image = models.ImageField(upload_to='articles')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
