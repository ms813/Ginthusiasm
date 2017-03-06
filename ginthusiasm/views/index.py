from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # Find out whether the user is over 18.
    # We use the COOKIES.get() function to obtain the 'verified' cookie.
    # If the cookie exists, the value returned is casted to a boolean.
    # If the cookie does not exist, then the default value 'False' is used.
    verified_age = bool(request.COOKIES.get('verified', False))
    return render(request, 'ginthusiasm/index.html', {'verified_age': verified_age})
