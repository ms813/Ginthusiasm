from django.shortcuts import render
from django.http import HttpResponse
from ginthusiasm.models import Article

#def article(request):
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
