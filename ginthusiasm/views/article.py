from django.shortcuts import render
from django.http import HttpResponse
from ginthusiasm.models import Article
from ginthusiasm.models import UserProfile
from django.contrib.auth.models import User
from ginthusiasm.forms import AddArticleForm
from datetime import date, datetime

#View for the main article page
def article(request, article_name_slug, user_name):

    context_dict={}
    check = User.objects.get(username=user_name).userprofile

    try:
        article = Article.objects.get(slug=article_name_slug, author=check)
        context_dict['article'] = article
        print(article)

    except Article.DoesNotExist:
        context_dict['article'] = None
        print("No article found")

    return render(request, 'ginthusiasm/article.html', context = context_dict)

def article_listing(request):

    context_dict = {}

    article = Article.objects.filter()
    context_dict['article'] = article

    # Go render the response and return it to the client.
    return render(request, 'ginthusiasm/article_listing.html', context_dict)

def article_user_listing(request, user_name):
    context_dict = {}
    check = User.objects.get(username=user_name).userprofile
    article = Article.objects.filter(author =check)

    context_dict['article'] = article

    # Go render the response and return it to the client.
    return render(request, 'ginthusiasm/article_listing.html', context_dict)

def article_month(request):
    context_dict = {}
    article = Article.objects.get(month =True)

    context_dict['article'] = article

    return render(request, 'ginthusiasm/article.html', context_dict)


# View for adding a gin to the database
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

    print(datetime.now)

    context_dict = {'add_article_form': form, 'user': user}
    return render(request, 'ginthusiasm/add_article.html', context=context_dict)
