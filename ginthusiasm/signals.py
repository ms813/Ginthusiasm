from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from ginthusiasm.models import Review

@receiver(post_save)
def callback(sender, **kwargs):
    r = kwargs['instance']
    if (isinstance(r, Review)):
        r.gin.update_average_rating()
