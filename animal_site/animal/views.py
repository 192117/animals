from django.shortcuts import render
from .models import Category, Animals

def list_category_animals(request):
    category = Category.objects.all()
    return render(request, 'category/category.html', context={'category': category})

def animal_detail(request, slug):
    animal = Animals.objects.get(slug=slug)
    return render(request, 'animal/animal_detail.html', context={'animal': animal})

def list_category(request, cat):
    id = Category.objects.get(name=cat)
    animals = Animals.objects.filter(category=id)
    return render(request, 'animal/animals.html', context={'animals': animals, 'cat': cat})

def list_animals(request,):
    animals = Animals.objects.all()
    return render(request, 'animal/animals.html', context={'animals': animals})