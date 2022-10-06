from django.shortcuts import render
from animal.models import Animals
from clients.models import Customer

def main_page(request):
    animals = Animals.objects.all().order_by('-rate')[:10]
    clients = Customer.objects.filter(role='Client')
    return render(request, 'main_page.html', context={'animals':animals, 'clients':clients})