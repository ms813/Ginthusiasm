from __future__ import unicode_literals
from django.db import models

"""
Represents an instance of user feedback, sent via the Contact Us page
"""


class Contact(models.Model):
    name = models.CharField(max_length=225, unique=True, blank=True)
    email = models.EmailField(blank=True)
    message = models.TextField(max_length=1000)
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.name, self.email)
