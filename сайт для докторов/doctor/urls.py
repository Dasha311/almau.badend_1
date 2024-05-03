from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page_view, name='index_page'),
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('doctors/<int:pk>/', views.doctor_details, name='doctor_details'),
    path('doctors/create/', views.create_doctor, name='create_doctor'),
    path('doctors/<int:pk>/edit/', views.edit_doctor, name='edit_doctor'),
    path('doctors/<int:pk>/delete/', views.delete_doctor, name='delete_doctor'),
    path('appointments/', views.appointments_list, name='appointments_list'),
    path('appointments/create/', views.create_appointment, name='create_appointment'),
    path('appointments/<int:pk>/edit/', views.edit_appointment, name='edit_appointment'),
    path('appointments/<int:pk>/delete/', views.delete_appointment, name='delete_appointment'),
]
