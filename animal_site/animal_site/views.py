from django.shortcuts import render
from animal.models import Animals
from clients.models import Customer
from news.models import News
from info.models import Info, SocialMedia, PriceList

def main_page(request):
    animals = Animals.objects.all().order_by('-rate')[:10]
    clients = Customer.objects.all()
    news = News.objects.all().order_by('-updated')[:5]
    info = Info.objects.get(pk=1)
    social = SocialMedia.objects.get(pk=1)
    price = PriceList.objects.get(pk=1)
    return render(request, 'main_page.html', context={'animals':animals, 'clients':clients, 'news':news,
                                                      'info':info, 'social':social, 'price':price})


