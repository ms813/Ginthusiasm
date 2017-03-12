import random

from django.db.models import Count, F
from django.shortcuts import render
from django.http import HttpResponse

from ginthusiasm.models import TasteTag, Gin

# SELECT *, COUNT(*) AS Count FROM ginthusiasm_tastetag AS GT
# LEFT JOIN ginthusiasm_gin_taste_tags AS GTT
# ON GT.id = GTT.tastetag_id
# GROUP BY GTT.tastetag_id
# ORDER BY Count DESC, name
# LIMIT 5;

def collections(request):
    taste_tag_names = Gin.objects.annotate(tag_name=F("taste_tags__name")).values("tag_name").annotate(count=Count("taste_tags")).order_by("-count")[:5]
    # print(taste_tag_names)
    # for each tag, find an associated gin and its image at random
    for tag_name in taste_tag_names:
        gins_with_tag = Gin.objects.filter(taste_tags__name=tag_name['tag_name'])
        tag_name['img'] = random.choice(gins_with_tag).image.url

    return render(request, 'ginthusiasm/collections.html', {"taste_tag_names": taste_tag_names})
