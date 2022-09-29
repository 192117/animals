from django.shortcuts import render

def main_list(request):
    return render(request, 'agency/base_base.html')