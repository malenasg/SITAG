from django.urls import path
from django.contrib.auth import logout
from django.shortcuts import redirect
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', lambda request: (logout(request), redirect('usuarios:login'))[1], name='logout'),
]
