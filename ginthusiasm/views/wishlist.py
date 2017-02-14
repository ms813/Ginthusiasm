from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from ginthusiasm.models import UserProfile, Wishlist

def wishlist(request, username):
    context = {"gins" : User.objects.get(username=username).userprofile.wishlist.gins.all}
    return render(request, 'ginthusiasm/wishlist.html', context)
