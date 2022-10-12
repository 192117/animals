from django.urls import path

from .views import lk_view

urlpatterns = [
    path('', lk_view, name='lk_url'),
]