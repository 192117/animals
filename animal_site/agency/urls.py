from django.urls import path

from .views import *

urlpatterns = [
    path('', main_list, name='agency_url'),
]