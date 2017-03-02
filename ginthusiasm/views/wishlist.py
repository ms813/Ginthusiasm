from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from ginthusiasm.models import UserProfile, Wishlist, Gin
from django.http import HttpResponse


def wishlist(request, username):
    user = User.objects.get(username=username)
    prof = user.userprofile

    context = {
        "wishlist_name": str(prof.wishlist),
        "gins": prof.wishlist.gins.all,
        "profile_image": prof.profile_image
    }

    if request.user.is_authenticated() and username == request.user.username:
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
            wl = request.user.userprofile.wishlist

            # Add or remove gin from wishlist
            if gin in wl.gins.all():
                response = "removed"
                wl.gins.remove(gin)
            else:
                response = "added"
                wl.gins.add(gin)

                wl.save()

            # return a status message letting the client know if the gin was added or removed
            return HttpResponse(response)
    else:
        # if user is not logged in, redirect them to the login page
        return redirect('login')
