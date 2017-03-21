import random

from django.db.models import Count, F
from django.shortcuts import render

from ginthusiasm.models.gin import Gin
from ginthusiasm.models import Article

"""
Renders the home page of the website

Includes multiple template widgets, requiring data from many models
"""


def index(request):
    # Find out whether the user is over 18.
    # We use the COOKIES.get() function to obtain the 'verified' cookie.
    # If the cookie exists, the value returned is cast to a boolean.
    # If the cookie does not exist, then the default value False is used.
    verified_age = bool(request.COOKIES.get('verified', False))
    trending_gins = Gin.objects.order_by('-average_rating')[:6]
    collection_highlights = Gin.objects.annotate(tag_name=F("taste_tags__name")).values("tag_name").annotate(count=Count("taste_tags")).order_by("-count")[:3]
    gin_month = Article.objects.filter(month=True)

    for tag_name in collection_highlights:
        gins_with_tag = Gin.objects.filter(taste_tags__name=tag_name['tag_name'])
        tag_name['img'] = random.choice(gins_with_tag).image.url

    context_dict = {
        'verified_age': verified_age,
        'trending_gins': trending_gins,
        'collection_highlights': collection_highlights,
        'gin_month':gin_month,
    }
    return render(request, 'ginthusiasm/index.html', context_dict)
