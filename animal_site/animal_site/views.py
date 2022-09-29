from django.shortcuts import redirect


def redirect_agency(request):
    return redirect('agency_url', permanent=True)