from django.urls import path

from .views import list_animals

urlpatterns = [
    path('', list_animal),
]