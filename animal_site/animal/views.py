from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Animals


def list_animals(request):
    animals = Animals.objects.all()
    return render(request, 'animal/animals.html', context={'animals': animals})

def animal_detail(request, slug):
    animal = Animals.objects.get(slug=slug)
    return render(request, 'animal/animal_detail.html', context={'animal': animal})


def animal_rate(request):
    print(request.POST)
    animal = Animals.objects.get(slug=request.POST['slug'])
    if request.POST['value'] == '+':
        animal.rate += 1
    elif request.POST['value'] =='-':
        if animal.rate > 0:
            animal.rate -= 1
    animal.save()
    # return render(request, 'animal/animal_detail.html', context={'animal': animal})