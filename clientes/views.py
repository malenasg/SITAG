from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Cliente
from .forms import ClienteForm

# Lista clientes
def lista_clientes(request):
    clientes = Cliente.objects.filter(activo=True)
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})

# Agregar cliente
def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.activo = True
            cliente.save()
            messages.success(request, "Datos cargados correctamente")
            return redirect('clientes:lista_clientes')
        else:
            # Los errores ahora aparecerán directamente sobre los campos
            messages.error(request, "Por favor corrija los errores del formulario")
    else:
        form = ClienteForm()

    return render(request, 'clientes/agregar_cliente.html', {'form': form})

# Editar cliente
def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.activo = True
            cliente.save()
            messages.success(request, "Se guardaron los datos correctamente.")
            return redirect('clientes:lista_clientes')
        else:
            messages.error(request, "Por favor corrija los errores del formulario")
    else:
        form = ClienteForm(instance=cliente)
    
    return render(request, 'clientes/editar_cliente.html', {'form': form, 'cliente': cliente})

def mostrar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    cliente.activo = True
    cliente.save()

    messages.success(request, "El cliente fue activado correctamente.")
    return redirect("clientes:clientes_ocultos")

def clientes_ocultos(request):
    clientes = Cliente.objects.filter(activo=False)
    return render(request, 'clientes/lista_ocultos.html', {'clientes': clientes})

def ocultar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.activo = False
    cliente.save()
    messages.info(request, f"El cliente fue ocultado exitosamente.")
    return redirect('clientes:lista_clientes')

