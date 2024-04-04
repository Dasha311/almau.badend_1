from django.contrib import admin
from django.urls import path

from .views import get_index_page, get_movie_details

urlpatterns = [
    path('', get_index_page),
    path('<int:pk>', get_movie_details),
]