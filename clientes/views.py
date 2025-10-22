from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteForm
from trabajos.models import Trabajo

# Detalle cliente
def detalle_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    trabajos = Trabajo.objects.filter(cliente=cliente, visible=True)
    return render(request, 'clientes/detalle_cliente.html', {'cliente': cliente, 'trabajos': trabajos})

# Lista clientes
def lista_clientes(request):
    clientes = Cliente.objects.filter(activo=True)
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})

# Agregar cliente
def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio:inicio')  
    else:
        form = ClienteForm()
    return render(request, 'clientes/agregar_cliente.html', {'form': form})

# Editar cliente
def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('clientes:lista_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/editar_cliente.html', {'form': form, 'cliente': cliente})

# Ocultar cliente
def ocultar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    cliente.activo = False
    cliente.save()
    return redirect('clientes:lista_clientes')

# Mostrar cliente
def mostrar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    cliente.activo = True
    cliente.save()
    return redirect('clientes:lista_clientes')
