from django.shortcuts import render
from ginthusiasm.models import Article
from django.contrib.auth.models import User
from ginthusiasm.forms import AddArticleForm
from datetime import date, datetime

"""
Views relating to the Article model, including creating new ones and Gin of the Month
"""


# View for the main article page
def article(request, article_name_slug, user_name):
    context_dict = {}
    check = User.objects.get(username=user_name).userprofile

    try:
        article = Article.objects.get(slug=article_name_slug, author=check)
        context_dict['article'] = article

    except Article.DoesNotExist:
        context_dict['article'] = None
        print("No article found")

    return render(request, 'ginthusiasm/article.html', context=context_dict)


# Renders a list of all articles
def article_listing(request):
    context_dict = {}

    article = Article.objects.order_by('-date')
    context_dict['article'] = article

    # Go render the response and return it to the client.
    return render(request, 'ginthusiasm/article_listing.html', context_dict)


# Renders a list of all articles written by a specified user
def article_user_listing(request, user_name):

    context_dict = {}
    check = User.objects.get(username=user_name).userprofile
    article = Article.objects.filter(author=check)

    context_dict['article'] = article

    # Go render the response and return it to the client.
    return render(request, 'ginthusiasm/article_listing.html', context_dict)

# Renders gin of the month page
def article_month(request):
    context_dict = {}
    article = Article.objects.get(month=True)

    context_dict['article'] = article

    return render(request, 'ginthusiasm/article.html', context_dict)

def add_article(request, user_name):
    try:
        user = User.objects.get(username=user_name)
        userprofile = user.userprofile
    except User.DoesNotExist:
        userprofile = None

    form = AddArticleForm()

    if request.method == 'POST':
        form = AddArticleForm(request.POST)
        if form.is_valid():
            if userprofile:
                article = form.save(commit=False)
                article.author = userprofile

                if 'image' in request.FILES:
                    article.image = request.FILES['image']

                article.save()
                return article_listing(request)

        else:
            print(form.errors)

    context_dict = {'add_article_form': form, 'user': user}
    return render(request, 'ginthusiasm/add_article.html', context=context_dict)
