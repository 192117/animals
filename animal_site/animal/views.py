from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Animals


def list_animals(request):
    animals = Animals.objects.all()
    paginator = Paginator(animals, 5)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''
    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url
    }
    return render(request, 'animal/animals.html', context=context)

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