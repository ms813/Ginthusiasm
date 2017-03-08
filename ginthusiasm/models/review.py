from __future__ import unicode_literals
from django.db import models
from user_profile import UserProfile

"""
Represents a Review, written by a User about a Gin

Each user can only write one review about each gin
"""


class Review(models.Model):
    # store the type of review, using the choices defined in the UserProfile
    review_type = models.CharField(
        max_length=1,
        choices=UserProfile.USER_TYPE_CHOICES,
        default=UserProfile.BASIC
    )

    date = models.DateField(blank=True, null=True)
    rating = models.PositiveSmallIntegerField(blank=True, null=True)

    # short text to be displayed in smaller widgets
    summary = models.CharField(max_length=1024, blank=True)

    # full body of the review
    content = models.TextField(blank=True)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    gin = models.ForeignKey('Gin', on_delete=models.CASCADE, related_name='reviews')

    class Meta:
        # use a combination of the user and the gin as primary key
        unique_together = ('user', 'gin',)

    def __str__(self):
        return self.user.user.username + ": " + self.gin.name

    def __unicode__(self):
        return self.user.user.username + ": " + self.gin.name
