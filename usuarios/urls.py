from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('', views.lista_usuarios, name='lista_usuarios'),
    path('agregar/', views.crear_usuario, name='crear_usuario'),
    path('editar/<int:id>/', views.editar_usuario, name='editar_usuario'),
    path('activar/<int:id>/', views.activar_usuario, name='activar_usuario'),
    path('desactivar/<int:id>/', views.desactivar_usuario, name='desactivar_usuario'),
    path('inactivos/', views.lista_usuarios_inactivos, name='lista_usuarios_inactivos'),
]
