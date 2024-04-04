from django.shortcuts import render
from .models import Article
# Create your views here.
def get_article_page(request):
    article = Article.objects.all()
    return render(request, 'blog/article.html', {'article': article} )

def get_article_details(request, pk):
    article = Article.objects.get(id=pk)
    return render(request, 'blog/article-details.html', {'article': article})