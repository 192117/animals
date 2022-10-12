from django.shortcuts import render

def lk_view(request):
    return render(request, 'users/lk.html')