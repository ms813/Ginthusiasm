from django.shortcuts import render
from django.http import HttpResponse

def article(request):
    return render(request, 'ginthusiasm/article.html')
