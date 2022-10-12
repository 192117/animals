from django.shortcuts import render
from .models import News
from info.models import Info, SocialMedia, PriceList

def news_page(request):
    news = News.objects.all()
    info = Info.objects.get(pk=1)
    social = SocialMedia.objects.get(pk=1)
    price = PriceList.objects.get(pk=1)
    return render(request, 'news/news.html', context={'news':news, 'info':info, 'social':social, 'price':price})


def news_detail(request, slug):
    news = News.objects.get(slug=slug)
    info = Info.objects.get(pk=1)
    social = SocialMedia.objects.get(pk=1)
    price = PriceList.objects.get(pk=1)
    return render(request, 'news/news_detail.html', context={'news': news, 'info':info, 'social':social, 'price':price})