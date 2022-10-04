from django.shortcuts import render
from animal.models import Animals

def main_page(request):
    animals = Animals.objects.all().order_by('-rate')[:10]
    return render(request, 'main_page.html', context={'animals':animals})