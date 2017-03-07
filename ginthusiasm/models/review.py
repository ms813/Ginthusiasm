from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Review(models.Model):
    # Single characters means less spaced used in DB
    BASIC = 'b'
    ADMIN = 'a'
    EXPERT = 'e'
    DISTILLERY_OWNER = 'o'

    # Tuple of tuples makes these choices immutable (can also be used to represent a single row from a database)
    # Maps user selection to variables above


    REVIEW_TYPE_CHOICES = (
        (BASIC, 'Basic user'),
        (ADMIN, 'Administrator'),
        (EXPERT, 'Expert reviewer'),
        (DISTILLERY_OWNER, 'Distillery Owner'),
    )

    review_type = models.CharField(
        max_length=1,
        choices=REVIEW_TYPE_CHOICES,
        default=BASIC
    )

    date = models.DateField(blank=True, null=True)
    rating = models.PositiveSmallIntegerField(blank=True, null=True)
    summary = models.CharField(max_length=1024, blank=True)
    content = models.TextField(blank=True)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    gin = models.ForeignKey('Gin', on_delete=models.CASCADE, related_name='reviews')



    @receiver(post_save)
    def callback(sender, **kwargs):
        print(kwargs)


    class Meta:
        unique_together = ('user', 'gin',)

    def __str__(self):
        return self.user.user.username + ": " + self.gin.name

    def __unicode__(self):
        return self.user.user.username + ": " + self.gin.name
