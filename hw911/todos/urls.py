from django.urls import path
from .views import todo_details_view, todo_page_view, delete_todo_page_view, index_page_view, basket_page_view, add_todo_to_basket_view, delete_from_basket_view


urlpatterns = [
    path('', index_page_view, name='index_page'),
    path('basket/', basket_page_view, name='basket'),
    path('add_to_basket/<int:pk>', add_todo_to_basket_view, name='add_to_basket'),
    path('delete_from_basket/<int:pk>', delete_from_basket_view, name='delete_from_basket'),
    path('todos/', todo_page_view, name='todo'),
    path('todos/<int:pk>', todo_details_view, name='todo_details'),
    path('todos/<int:pk>/delete', delete_todo_page_view, name='delete_todo_page')


]