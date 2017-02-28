from django.shortcuts import render
from django.http import HttpResponse
from ginthusiasm.models import Article

#View for the main article page
def article(request, article_name_slug):

    context_dict={}

    try:
        article = Article.objects.get(slug=article_name_slug)
        context_dict['article'] = article
        print(article)

    except Article.DoesNotExist:
        context_dict['article'] = None
        print("No article found")

    return render(request, 'ginthusiasm/article.html', context = context_dict)

def article_listing(request):
    context_dict = {}

    articles = Article.objects.filter()
    context_dict['article'] = articles

    # Go render the response and return it to the client.
    return render(request, 'ginthusiasm/article_listing.html', context_dict)
