from django.urls import path
from . import views

app_name = 'trabajos'

urlpatterns = [
    path('', views.lista_trabajos, name='lista_trabajos'),
    path('agregar/', views.agregar_trabajo, name='agregar'),
    path('editar/<int:trabajo_id>/', views.editar_trabajo, name='editar'),
    path('ver/<int:trabajo_id>/', views.detalle_trabajo, name='detalle'),
]
