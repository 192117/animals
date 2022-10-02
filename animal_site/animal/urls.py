from django.urls import path

from .views import list_animals, animal_detail

urlpatterns = [
    path('', list_animals),
    path('animal/<str:slug>/', animal_detail, name='animal_detail_url'),
]