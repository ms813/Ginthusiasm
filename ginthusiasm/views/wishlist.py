from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from ginthusiasm.models import UserProfile, Wishlist, Gin
from django.http import HttpResponse

def wishlist(request, username):
    context = {"gins" : User.objects.get(username=username).userprofile.wishlist.gins.all}
    return render(request, 'ginthusiasm/wishlist.html', context)

# handles POST requests from 'add to/remove from wishlist' button
def wishlist_add(request, gin_slug):
    response = "unauthenticated"

    # if the user is logged in
    if not request.user.is_anonymous():
        wishlist = request.user.userprofile.wishlist
        gin = Gin.objects.get(slug=gin_slug)

        # check if gin is already on this wishlist
        if gin in wishlist.gins.all():
            response = "removed"
            wishlist.gins.remove(gin)
        else:
            response = "added"
            wishlist.gins.add(gin)
        wishlist.save()

        if request.method == 'POST':
            return HttpResponse(response)
        else:
            return redirect('wishlist', request.user.username)

    else:
        # if user is not logged in, redirect them to the login page
        return redirect('login')
