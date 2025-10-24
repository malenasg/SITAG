from django.urls import path
from . import views as auth_views

app_name = 'usuarios'

urlpatterns = [
    path('login/', auth_views.login_view, name='login'),
    path('logout/', auth_views.logout_view, name='logout'),

    path('', auth_views.lista_usuarios, name='lista_usuarios'),
]
