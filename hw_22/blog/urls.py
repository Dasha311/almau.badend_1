from django.contrib import admin
from django.urls import path

from .views import get_article_page, get_article_details

urlpatterns = [
    path('', get_article_page),
    path('<int:pk>', get_article_details),
]