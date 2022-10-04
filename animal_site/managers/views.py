from django.shortcuts import render
from .models import Manager
from clients.models import Customer


def about_managers(request):
    if request.method == 'GET':
        managers = Manager.objects.all()
        clients = Customer.objects.filter(review__isnull=False)
        return render(request, 'managers/managers.html', context={'managers': managers, 'clients':clients})
