from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UsuarioForm
from usuarios.forms import CustomLoginForm

Usuario = get_user_model()

def login_view(request):
    print("ENTRÓ A MI LOGIN")

    form = CustomLoginForm(request, data=request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Inicio de sesión exitoso.")
            return redirect("inicio:inicio")

    return render(request, 'registration/login.html', {"form": form})

@login_required(login_url='usuarios:login')
def logout_view(request):
    logout(request)
    return redirect('usuarios:login')

def lista_usuarios(request):
    usuarios = Usuario.objects.filter(is_active=True)
    context = {
        'usuarios': usuarios
    }
    return render(request, 'usuarios/lista_usuarios.html', context)

def crear_usuario(request):
    if request.method == 'POST':
        nombre_completo = request.POST['nombre_completo']
        username = request.POST['username']
        email = request.POST['email']
        rol = request.POST['rol']
        activo = request.POST.get('activo') == 'on'
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Las contraseñas no coinciden")
            return redirect('usuarios:crear_usuario')

        if Usuario.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya existe")
            return redirect('usuarios:crear_usuario')

        user = Usuario(
            username=username,
            first_name=nombre_completo,
            email=email,
            rol=rol,
            is_active=activo
        )
        user.set_password(password1) 
        user.save()

        messages.success(request, "Usuario creado correctamente.")
        return redirect("usuarios:lista_usuarios")

    return render(request, "usuarios/crear_usuario.html")

def editar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)

    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario actualizado correctamente.")
            return redirect('usuarios:lista_usuarios')
    else:
        form = UsuarioForm(instance=usuario)

    return render(request, 'usuarios/editar_usuario.html', {'form': form, 'usuario': usuario})

def lista_usuarios(request):
    usuarios = Usuario.objects.filter(is_active=True)
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})

def desactivar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    usuario.is_active = False
    usuario.save()
    messages.info(request, f"Usuario desactivado.")
    return redirect('usuarios:lista_usuarios')


def activar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    usuario.is_active = True
    usuario.save()
    messages.success(request, f"Usuario activado.")
    return redirect('usuarios:lista_usuarios_inactivos')

def lista_usuarios_inactivos(request):
    usuarios = Usuario.objects.filter(is_active=False)
    return render(request, 'usuarios/lista_inactivos.html', {'usuarios': usuarios})
