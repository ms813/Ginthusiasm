from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from ginthusiasm.models import Review

# called every time a model is saved
@receiver(post_save)
def callback(sender, **kwargs):
    r = kwargs['instance']

    # Used to update Gin average ratings when a Review is saved
    if (isinstance(r, Review)):
        r.gin.update_average_rating()
