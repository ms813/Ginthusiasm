from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from ginthusiasm.models import Gin, Review


@login_required
def my_reviews(request, username):
    reviewer = User.objects.filter(username=username).first()
    reviews = reviewer.userprofile.reviews.all()

    context = {
        "reviews": reviews,
        "reviewer": reviewer
    }

    return render(request, 'ginthusiasm/my_reviews.html', context)
