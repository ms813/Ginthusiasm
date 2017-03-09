from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from ginthusiasm.forms import UserForm, LoginForm, UploadFileForm
from ginthusiasm.models import UserProfile, Wishlist, Distillery

"""
Views in this file handle login and signup requests from users
"""


# Responds to login requests, redirecting the user to their account page if successful
# Or displays an error if login is unsuccessful
def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(data=request.POST)

        if login_form.is_valid():
            userdata = login_form.cleaned_data

            # check the user's credentials are legit
            user = authenticate(username=userdata.get('username'), password=userdata.get('password'))

            if user:
                login(request, user)
                return redirect('myaccount')
            else:
                # bad login credentials
                # only pass login form to template, assume user doesn't want to sign up
                context = {
                    'login_form': LoginForm(),
                    'error': 'Invalid username and password combination!',
                }
                return render(request, 'ginthusiasm/login.html', context)
        else:
            # invalid form data
            pass

    else:
        # probably GET request, render the login and signup forms
        context = {
            'login_form': LoginForm(),
            'user_form': UserForm()
        }
        return render(request, 'ginthusiasm/login.html', context)


# Creates a new user if the supplied information is value
# Creates a wishlist for the new user
def signup(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = UserProfile()
            profile.user = user

            profile.save()

            # create an empty wishlist for the new user
            wishlist = Wishlist(user=profile)
            wishlist.save()

            # new user is good, log them in
            login(request, user)
            return redirect('myaccount')
        else:
            # bad sign up data, render the form and the errors
            # only pass signup form to template, assume user doesn't want to login
            context = {
                "error": user_form.errors,
                'user_form': UserForm()
            }
            return render(request, 'ginthusiasm/login.html', context)
    else:
        # if not a post request, redirect to login page
        return redirect('login')


# The user's account page
# Contains links to user's wishlist, articles etc
# Profile picture can be changed from this page
@login_required
def myaccount(request):
    userprofile = request.user.userprofile
    context = {}

    if request.method == 'POST':

        # Update the user's profile picture
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            if 'profile_image' in request.FILES:
                userprofile.profile_image = request.FILES['profile_image']
                userprofile.save()
        else:
            # invalid form data
            print("Error uploading profile image", form.errors)
    else:
        # the upload profile image form
        context['form'] = UploadFileForm()

        # check if the user owns any distilleries
        if userprofile.user_type == UserProfile.DISTILLERY_OWNER:
            context['distilleries'] = Distillery.objects.filter(owner=userprofile)
        elif userprofile.user_type == UserProfile.ADMIN:
            context['distilleries'] = Distillery.objects.all()


    return render(request, 'ginthusiasm/myaccount.html', context)


# Log the current user out
@login_required
def user_logout(request):
    logout(request)
    return redirect('index')
