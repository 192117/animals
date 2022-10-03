from django.urls import path

from .views import model_view, photo_view

urlpatterns = [
    path('photo/', photo_view, name='photo_create_url'),
    path('model/', model_view, name='model_create_url'),
]