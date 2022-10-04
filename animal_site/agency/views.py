from django.template import RequestContext

from .forms import OrderForm, ModelForm
from django.shortcuts import render, redirect


def result_view(request):
    return render(request, 'agency/success_page.html')


def model_view(request):
    if request.method == 'POST':
        bound_form = ModelForm(request.POST, request.FILES)
        if bound_form.is_valid():
            new_obj = bound_form.save()
            return result_view(request)
        return render(request, 'agency/model_create.html', context={'form': bound_form})
    else:
        bound_form = OrderForm()
        return render(request, 'agency/order_create.html', context={'form': bound_form})


def photo_view(request):
    if request.method == 'POST':
        bound_form = OrderForm(request.POST)
        if bound_form.is_valid():
            new_obj = bound_form.save()
            return result_view(request)
        return render(request, 'agency/order_create.html', context={'form': bound_form})
    else:
        bound_form = OrderForm()
        return render(request, 'agency/order_create.html', context={'form': bound_form})


def contacts(request):
    return render(request, 'agency/contact.html')


