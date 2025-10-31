from django.urls import path
from . import views as auth_views

app_name = 'usuarios'

urlpatterns = [
    path('login/', auth_views.login_view, name='login'),
    path('logout/', auth_views.logout_view, name='logout'),

    path('', auth_views.lista_usuarios, name='lista_usuarios'),
    path('agregar/', auth_views.crear_usuario, name='crear_usuario'),
    path('editar/<int:id>/', auth_views.editar_usuario, name='editar_usuario'),
    path('activar/<int:id>/', auth_views.activar_usuario, name='activar_usuario'),
    path('desactitvar/<int:id>/', auth_views.desactivar_usuario, name='desactivar_usuario'),
    path('inactivos/', auth_views.lista_usuarios_inactivos, name='lista_usuarios_inactivos'),
    ]
