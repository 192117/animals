from django.urls import path

from .views import list_category_animals, animal_detail, list_category, list_animals

urlpatterns = [
    path('', list_category_animals, name='category_list_url'),
    path('all/', list_animals, name='animals_url'),
    path('<str:cat>/', list_category, name='animals_category_url'),
    path('animal/<str:slug>/', animal_detail, name='animal_detail_url'),
]