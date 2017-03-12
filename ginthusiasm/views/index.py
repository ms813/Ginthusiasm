from django.shortcuts import render

from ginthusiasm.models.gin import Gin

"""
Renders the home page of the website

Includes multiple template widgets, requiring data from many models
"""


def index(request):
    # Find out whether the user is over 18.
    # We use the COOKIES.get() function to obtain the 'verified' cookie.
    # If the cookie exists, the value returned is casted to a boolean.
    # If the cookie does not exist, then the default value 'False' is used.
    verified_age = bool(request.COOKIES.get('verified', False))
    trending_gins = Gin.objects.order_by('-average_rating')[:3]

    context_dict = {
        'verified_age': verified_age,
        'trending_gins': trending_gins,
    }
    return render(request, 'ginthusiasm/index.html', context_dict)
