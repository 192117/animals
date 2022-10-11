from django.shortcuts import render
from .models import News

def news_page(request):
    news = News.objects.all()
    return render(request, 'news/news.html', context={'news':news})


def news_detail(request, slug):
    news = News.objects.get(slug=slug)
    return render(request, 'news/news_detail.html', context={'news': news})