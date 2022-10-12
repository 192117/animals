from .forms import OrderForm, ModelForm
from django.shortcuts import render, redirect
from info.models import Info, SocialMedia, PriceList

def result_view(request):
    info = Info.objects.get(pk=1)
    social = SocialMedia.objects.get(pk=1)
    price = PriceList.objects.get(pk=1)
    return render(request, 'agency/success_page.html', context={'info':info, 'social':social, 'price':price})


def model_view(request):
    info = Info.objects.get(pk=1)
    social = SocialMedia.objects.get(pk=1)
    price = PriceList.objects.get(pk=1)
    if request.method == 'POST':
        bound_form = ModelForm(request.POST, request.FILES)
        if bound_form.is_valid():
            new_obj = bound_form.save()
            return result_view(request)
        return render(request, 'agency/model_create.html', context={'bound_form': bound_form, 'info':info, 'social':social, 'price':price})
    else:
        bound_form = ModelForm()
        return render(request, 'agency/model_create.html', context={'bound_form': bound_form, 'info':info, 'social':social, 'price':price})


def photo_view(request):
    info = Info.objects.get(pk=1)
    social = SocialMedia.objects.get(pk=1)
    price = PriceList.objects.get(pk=1)
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            new_obj = form.save()
            return result_view(request)
        return render(request, 'agency/order_create.html', context={'form': form, 'info':info, 'social':social, 'price':price})
    else:
        form = OrderForm()
        return render(request, 'agency/order_create.html', context={'form': form, 'info':info, 'social':social, 'price':price})


def contacts(request):
    info = Info.objects.get(pk=1)
    social = SocialMedia.objects.get(pk=1)
    price = PriceList.objects.get(pk=1)
    return render(request, 'agency/contact.html', context={'info':info, 'social':social, 'price':price})


