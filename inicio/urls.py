from django.urls import path
from . import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('agregar_cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('pendientes/', views.trabajos_pendientes, name='pendientes'),
]
