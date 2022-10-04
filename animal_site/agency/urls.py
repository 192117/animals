from django.urls import path

from .views import model_view, photo_view, result_view, contacts

urlpatterns = [
    path('photo/', photo_view, name='photo_create_url'),
    path('model/', model_view, name='model_create_url'),
    path('success/', result_view, name='result_order_url'),
    path('contacts/', contacts, name='contact_url')
]