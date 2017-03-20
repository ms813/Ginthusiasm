from django.shortcuts import render
from ginthusiasm.models import Article
from django.contrib.auth.models import User
from ginthusiasm.models import UserProfile
from ginthusiasm.forms import AddArticleForm
from datetime import date, datetime
from django.contrib.auth.decorators import login_required

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

    if check.user_type == UserProfile.BASIC:
        # basic users are not allowed to write articles, so redirect them to the article archive
        # and show an error message
        print("User " + str(check) + " doesn't have sufficient permissions to write articles!")
        context_dict['article'] = Article.objects.order_by('-date')
        context_dict['invalid_user'] = check.user.username
        return render(request, 'ginthusiasm/article_listing.html', context_dict)
    else:
        context_dict['article'] = article

        # Go render the response and return it to the client.
        return render(request, 'ginthusiasm/article_listing.html', context_dict)


# Renders gin of the month page
def article_month(request):
    context_dict = {}
    article = Article.objects.get(month=True)

    context_dict['article'] = article

    return render(request, 'ginthusiasm/article.html', context_dict)

@login_required
def add_article(request, user_name):
    try:
        user = User.objects.get(username=user_name)
        userprofile = user.userprofile
    except User.DoesNotExist:
        userprofile = None

    form = AddArticleForm()

    if request.user.is_anonymous():
        return article_listing(request)

    is_expert = request.user.userprofile.user_type == UserProfile.EXPERT
    is_admin = request.user.userprofile.user_type == UserProfile.ADMIN

    # if the user doesnt have privileges, send them to the distillery page
    if not (is_admin or is_expert):
        return article_listing(request)

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
