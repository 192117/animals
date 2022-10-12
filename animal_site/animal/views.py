from django.shortcuts import render
from .models import Category, Animals
from info.models import Info, SocialMedia, PriceList

def list_category_animals(request):
    category = Category.objects.all()
    info = Info.objects.get(pk=1)
    social = SocialMedia.objects.get(pk=1)
    price = PriceList.objects.get(pk=1)
    return render(request, 'category/category.html', context={'category': category, 'info':info, 'social':social, 'price':price})

def animal_detail(request, slug):
    animal = Animals.objects.get(slug=slug)
    info = Info.objects.get(pk=1)
    social = SocialMedia.objects.get(pk=1)
    price = PriceList.objects.get(pk=1)
    return render(request, 'animal/animal_detail.html', context={'animal': animal, 'info':info, 'social':social, 'price':price})

def list_category(request, cat):
    id = Category.objects.get(name=cat)
    animals = Animals.objects.filter(category=id)
    info = Info.objects.get(pk=1)
    social = SocialMedia.objects.get(pk=1)
    price = PriceList.objects.get(pk=1)
    return render(request, 'animal/animals.html', context={'animals': animals, 'cat': cat, 'info':info, 'social':social, 'price':price})

def list_animals(request,):
    animals = Animals.objects.all()
    info = Info.objects.get(pk=1)
    social = SocialMedia.objects.get(pk=1)
    price = PriceList.objects.get(pk=1)
    return render(request, 'animal/animals.html', context={'animals': animals, 'info':info, 'social':social, 'price':price})