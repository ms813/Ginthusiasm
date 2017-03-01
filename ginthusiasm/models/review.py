from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.db import models

class Review(models.Model):
    # Single characters means less spaced used in DB
    EXPERT = 'e'
    USER = 'u'

    # Tuple of tuples makes these choices immutable (can also be used to represent a single row from a database)
    # Maps user selection to variables above
    REVIEW_TYPE_CHOICES = (
        (EXPERT, 'Expert review'),
        (USER, 'User review'),
    )

    review_type = models.CharField(
        max_length=1,
        choices = REVIEW_TYPE_CHOICES,
        default = USER
    )

    date = models.DateField(blank=True)
    rating = models.PositiveSmallIntegerField(blank=True)
    summary = models.CharField(max_length=1024, blank=True)
    content = models.TextField(blank=True)
    lat = models.FloatField(blank=True)
    long = models.FloatField(blank=True)
    slug = models.SlugField(unique=True)
    # Assuming that when a user deletes their profile they'll want all their
    # reviews deleted too. Not sure about the foreign key argument?
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    gin = models.ForeignKey('Gin', on_delete=models.CASCADE, related_name='reviews')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Review, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
