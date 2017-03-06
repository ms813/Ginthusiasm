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

    date = models.DateField(blank=True, null=True)
    rating = models.PositiveSmallIntegerField(blank=True, null=True)
    summary = models.CharField(max_length=1024, blank=True)
    content = models.TextField(blank=True)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    #slug = models.SlugField(unique=True)
    # Assuming that when a user deletes their profile they'll want all their
    # reviews deleted too.
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    gin = models.ForeignKey('Gin', on_delete=models.CASCADE, related_name='reviews')

    class Meta:
        unique_together = ('user', 'gin',)

    #def save(self, *args, **kwargs):
            #self.slug = slugify(self.name)
        #super(Review, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.user.username + ": " + self.gin.name

    def __unicode__(self):
        return self.user.user.username + ": " + self.gin.name
