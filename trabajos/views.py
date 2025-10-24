from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from datetime import date, timedelta

from .models import Trabajo, Plano, Cuenta
from .forms import TrabajoForm, UbicacionForm
from clientes.models import Cliente


# 🔹 Lista de trabajos
def lista_trabajos(request):
    trabajos = Trabajo.objects.filter(visible=True)
    clientes = Cliente.objects.filter(activo=True)

    # Filtros
    cliente_id = request.GET.get('cliente')
    estado = request.GET.get('estado')
    palabra = request.GET.get('buscar')

    if cliente_id and cliente_id != 'todos':
        trabajos = trabajos.filter(cliente_id=cliente_id)

    if estado and estado != 'todos':
        trabajos = trabajos.filter(estado=estado)

    if palabra:
        trabajos = trabajos.filter(descripcion__icontains=palabra)

    return render(request, 'trabajos/lista_trabajos.html', {
        'trabajos': trabajos,
        'clientes': clientes,
    })


# 🔹 Ocultar un trabajo (marcar visible=False)
def ocultar_trabajo(request, id):
    trabajo = get_object_or_404(Trabajo, id=id)
    trabajo.visible = False
    trabajo.save()
    messages.success(request, "El trabajo fue ocultado correctamente.")
    return redirect('trabajos:lista_trabajos')


# 🔹 Editar un trabajo existente
def editar_trabajo(request, trabajo_id):
    trabajo = get_object_or_404(Trabajo, id=trabajo_id)
    if request.method == 'POST':
        form = TrabajoForm(request.POST, instance=trabajo)
        if form.is_valid():
            form.save()
            messages.success(request, "Trabajo actualizado correctamente.")
            return redirect('trabajos:lista_trabajos')
    else:
        form = TrabajoForm(instance=trabajo)
    return render(request, 'trabajos/editar_trabajo.html', {'form': form, 'trabajo': trabajo})


# 🔹 Ver trabajos pendientes de esta semana
def pendientes_semana(request):
    hoy = date.today()
    fin_semana = hoy + timedelta(days=7)
    trabajos = Trabajo.objects.filter(
        estado='Pendiente',
        fecha_inicio__range=[hoy, fin_semana],
        visible=True
    )
    return render(request, 'trabajos/pendientes_semana.html', {'trabajos': trabajos})


# 🔹 Detalle de un trabajo (cliente, planos, cuentas)
def detalle_trabajo(request, trabajo_id):
    trabajo = get_object_or_404(Trabajo, id=trabajo_id)
    cliente = trabajo.cliente
    planos = Plano.objects.filter(trabajo=trabajo)
    cuentas = Cuenta.objects.filter(trabajo=trabajo)

    return render(request, 'trabajos/detalles_trabajo.html', {
        'trabajo': trabajo,
        'cliente': cliente,
        'planos': planos,
        'cuentas': cuentas,
    })


# 🔹 Agregar nuevo trabajo + ubicación
def agregar_trabajo(request):
    if request.method == 'POST':
        trabajo_form = TrabajoForm(request.POST)
        ubicacion_form = UbicacionForm(request.POST)

        if trabajo_form.is_valid() and ubicacion_form.is_valid():
            ubicacion = ubicacion_form.save()
            trabajo = trabajo_form.save(commit=False)
            trabajo.ubicacion = ubicacion
            trabajo.save()
            messages.success(request, "Trabajo creado correctamente.")
            return redirect('trabajos:lista_trabajos')
        else:
            messages.error(request, "Por favor, corregí los errores del formulario.")
    else:
        trabajo_form = TrabajoForm()
        ubicacion_form = UbicacionForm()

    return render(request, 'trabajos/agregar_trabajo.html', {
        'trabajo_form': trabajo_form,
        'ubicacion_form': ubicacion_form
    })
