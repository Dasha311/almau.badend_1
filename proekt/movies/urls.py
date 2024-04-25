from django.urls import path
from .views import movies_page_view, movie_details_page_view, delete_movies_page_view, edit_movies_page_view, \
    index_page_view, cart_page_view, add_movie_to_cart_view, delete_from_cart_view

urlpatterns = [
    path('', index_page_view, name='index_page'),
    path('cart/', cart_page_view, name='cart'),
    path('add_to_cart/<int:pk>', add_movie_to_cart_view, name='add_to_cart'),
    path('delete_from_cart/<int:pk>', delete_from_cart_view, name='delete_from_cart'),
    path('movies/', movies_page_view, name='movies_page'),
    path('movies/<int:pk>/', movie_details_page_view, name='movie_details_page'),
    path('movies/<int:pk>/edit/', edit_movies_page_view, name='edit_movie_page'),
    path('movies/<int:pk>/delete/', delete_movies_page_view, name='delete_movie_page')
]
