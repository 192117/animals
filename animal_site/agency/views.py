from .forms import OrderForm, ModelForm
from django.shortcuts import render, redirect

def model_view(request):
    bound_form = ModelForm(request.POST)
    if bound_form.is_valid():
        new_obj = bound_form.save()
        return redirect(new_obj)
    return render(request, 'agency/model_create.html', context={'form': bound_form})


def photo_view(request):
    bound_form = OrderForm(request.POST)
    if bound_form.is_valid():
        new_obj = bound_form.save()
        return redirect(new_obj)
    return render(request, 'agency/order_create.html', context={'form': bound_form})


