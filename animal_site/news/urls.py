from django.urls import path

from .views import news_page, news_detail

urlpatterns = [
    path('', news_page, name='news_page_url'),
    path('<str:slug>/', news_detail, name='news_detail_url'),
]