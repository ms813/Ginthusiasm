from django.shortcuts import render

"""
Renders the about page
"""


def about(request):
    return render(request, 'ginthusiasm/about.html')
