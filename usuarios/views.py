from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from .models import Usuario

def login_view(request):
    if request.user.is_authenticated:
        return redirect('inicio:dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio:dashboard')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')

    return render(request, 'registration/login.html')


@login_required(login_url='usuarios:login')
def logout_view(request):
    logout(request)
    return redirect('usuarios:login')


@login_required(login_url='usuarios:login')
def index(request):
    return render(request, 'usuarios/index.html')

def lista_usuarios(request):
    usuarios = Usuario.objects.filter(activo=True)
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})