from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from ginthusiasm.forms import UserForm, LoginForm
from ginthusiasm.models import UserProfile, Wishlist

def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(data=request.POST)

        if login_form.is_valid():
            userdata=login_form.cleaned_data
            user = authenticate(username = userdata.get('username'), password = userdata.get('password'))

            if user:
                login(request, user)
                return redirect('myaccount')
            else:
                # bad login credentials
                context = {
                    'login_form': LoginForm(),
                    'error' : 'Invalid username and password combination!',
                }
                return render(request, 'ginthusiasm/login.html', context)
        else:
            # invalid form data
            pass

    else:
        context = {
            'login_form' : LoginForm(),
            'user_form': UserForm()
        }
        return render(request, 'ginthusiasm/login.html', context)

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
            # context = {'message' : 'Account created!', 'login_form' : LoginForm()}
            # return render(request, 'ginthusiasm/login.html', context)
        else:
            # bad sign up data
            context = {
                "error" : user_form.errors,
                'user_form' : UserForm()
            }
            return render(request, 'ginthusiasm/login.html', context)
    else:
        # if not a post request, redirect to login page
        return redirect('login')

@login_required
def myaccount(request):
    return render(request, 'ginthusiasm/myaccount.html', {})

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')
