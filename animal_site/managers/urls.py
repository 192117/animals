from django.urls import path

from .views import about_managers

urlpatterns = [
    path('', about_managers, name='managers_list_url'),
]