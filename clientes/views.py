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
            messages.success(request, "Cliente agregado correctamente")
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
            messages.success(request, "Cliente actualizado correctamente")
            return redirect('clientes:lista_clientes')
        else:
            messages.error(request, "Por favor corrija los errores del formulario")
    else:
        form = ClienteForm(instance=cliente)
    
    return render(request, 'clientes/editar_cliente.html', {'form': form, 'cliente': cliente})

# Ocultar cliente
def ocultar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    cliente.activo = False
    cliente.save()
    messages.success(request, "Cliente ocultado correctamente")
    return redirect('clientes:lista_clientes')
