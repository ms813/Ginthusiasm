from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from ginthusiasm.models import UserProfile, Wishlist, Gin
from django.http import HttpResponse

def wishlist(request, username):
    wishlist = User.objects.get(username=username).userprofile.wishlist
    context = {
        "wishlist_name" : str(wishlist),
        "gins" : wishlist.gins.all
    }

    if request.user.is_authenticated():
        context['wishlist_name'] = "Your wishlist"

    return render(request, 'ginthusiasm/wishlist.html', context)

# handles requests from 'add to/remove from wishlist' button
def wishlist_add(request):
    # if the user is logged in
    if not request.user.is_anonymous():
        if not request.method == 'POST':
            # if the user sends a GET request, redirect them to their own wishlist
            return redirect('wishlist', request.user.username)
        else:
            # user is sending a POST request, so probably clicked the button

            # get the gin slug from the body of the post request
            gin_slug = request.POST['gin_slug']

            # find the Gin object matching the slug
            gin = Gin.objects.get(slug=gin_slug)

            # find the current user's wishlist
            wishlist = request.user.userprofile.wishlist

            # Add or remove gin from wishlist
            if gin in wishlist.gins.all():
                response = "removed"
                wishlist.gins.remove(gin)
            else:
                response = "added"
                wishlist.gins.add(gin)

            wishlist.save()

            # return a status message letting the client know if the gin was added or removed
            return HttpResponse(response)
    else:
        # if user is not logged in, redirect them to the login page
        return redirect('login')
