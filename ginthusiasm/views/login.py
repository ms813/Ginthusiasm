from django.shortcuts import render
from django.http import HttpResponse

def login(request):

    return render(request, 'ginthusiasm/login.html')
