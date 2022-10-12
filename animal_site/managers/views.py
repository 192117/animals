from django.shortcuts import render
from .models import Manager
from clients.models import Customer
from info.models import Info, SocialMedia, PriceList


def about_managers(request):
    info = Info.objects.get(pk=1)
    social = SocialMedia.objects.get(pk=1)
    price = PriceList.objects.get(pk=1)
    if request.method == 'GET':
        managers = Manager.objects.filter(photo__isnull=False)
        clients = Customer.objects.filter(review__isnull=False)
        return render(request, 'managers/managers.html', context={'managers': managers, 'clients':clients,
                                                                  'info':info, 'social':social, 'price':price})
