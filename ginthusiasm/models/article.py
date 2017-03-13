from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify

"""
Represents a news or feature article written by a User

Each article can only have one author
"""


class Article(models.Model):
    title = models.CharField(max_length=128, unique=True)

    # strap line used in small widgets
    shortDesc = models.TextField(max_length=1000, unique=True)

    # full content of the article body
    content = models.TextField(max_length=1000)
    date = models.DateField()
    slug = models.SlugField(max_length=50, unique=True)
    author = models.ForeignKey('UserProfile', related_name='article')
    image = models.ImageField(upload_to='articles', blank=True, null=True)

    # True if this article is the featured article of the month
    month = models.BooleanField()

    # override the save method to automatically set the slug based on the name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
