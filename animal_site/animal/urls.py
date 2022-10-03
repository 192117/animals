from django.urls import path

from .views import list_animals, animal_detail, animal_rate

urlpatterns = [
    path('', list_animals, name='animals_list_url'),
    path('animal/<str:slug>/', animal_detail, name='animal_detail_url'),
    path('rate/', animal_rate, name='animal_rate_url'),
]