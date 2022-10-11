from django.shortcuts import render
from animal.models import Animals
from clients.models import Customer
from news.models import News

def main_page(request):
    animals = Animals.objects.all().order_by('-rate')[:10]
    clients = Customer.objects.all()
    news = News.objects.all().order_by('-updated')[:5]
    return render(request, 'main_page.html', context={'animals':animals, 'clients':clients, 'news':news})


def faq_view(request):
    return render(request, 'faq.html')

