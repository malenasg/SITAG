from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from clientes.models import Cliente
from trabajos.models import Trabajo, Ubicacion, Plano
from .forms import TrabajoForm, UbicacionForm


def lista_trabajos(request):
    trabajos = Trabajo.objects.all()
    clientes = Cliente.objects.filter(activo=True)

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


def agregar_trabajo(request):
    if request.method == 'POST':
        trabajo_form = TrabajoForm(request.POST)
        ubicacion_form = UbicacionForm(request.POST)

        if trabajo_form.is_valid() and ubicacion_form.is_valid():
            trabajo = trabajo_form.save(commit=False)

            # Guardar ubicación solo si se cargó algo
            if ubicacion_form.has_changed():
                ubicacion = ubicacion_form.save()
                trabajo.ubicacion = ubicacion

            trabajo.save()

            messages.success(request, "Trabajo guardado correctamente.")
            return redirect('trabajos:lista_trabajos')
        else:
            messages.error(request, "Faltan completar campos, revise e inténtelo nuevamente.")
    else:
        trabajo_form = TrabajoForm()
        ubicacion_form = UbicacionForm()

    return render(request, 'trabajos/agregar_trabajo.html', {
        'trabajo_form': trabajo_form,
        'ubicacion_form': ubicacion_form,
    })


def editar_trabajo(request, trabajo_id):
    trabajo = get_object_or_404(Trabajo, id=trabajo_id)
    ubicacion = trabajo.ubicacion

    if request.method == "POST":
        trabajo_form = TrabajoForm(request.POST, instance=trabajo)
        ubicacion_form = UbicacionForm(request.POST, instance=ubicacion)

        if trabajo_form.is_valid() and ubicacion_form.is_valid():
            trabajo = trabajo_form.save(commit=False)

            if ubicacion_form.has_changed():
                ubicacion = ubicacion_form.save()
                trabajo.ubicacion = ubicacion

            trabajo.save()

            messages.success(request, "Se guardaron los datos correctamente.")
            return redirect('trabajos:lista_trabajos')
        else:
            messages.error(request, "Por favor corrija los errores del formulario.")
    else:
        trabajo_form = TrabajoForm(instance=trabajo)
        ubicacion_form = UbicacionForm(instance=ubicacion)

    return render(request, 'trabajos/editar_trabajo.html', {
        'trabajo_form': trabajo_form,
        'ubicacion_form': ubicacion_form,
        'trabajo': trabajo,
    })


def detalle_trabajo(request, trabajo_id):
    trabajo = get_object_or_404(Trabajo, id=trabajo_id)
    cliente = trabajo.cliente
    planos = Plano.objects.filter(trabajo=trabajo)

    return render(request, 'trabajos/detalles_trabajo.html', {
        'trabajo': trabajo,
        'cliente': cliente,
        'planos': planos,
    })
