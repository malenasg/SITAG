from django.shortcuts import render, redirect, get_object_or_404
from .models import Trabajo
from .forms import TrabajoForm
from clientes.models import Cliente
from datetime import date, timedelta

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

def ocultar_trabajo(request, id):
    trabajo = get_object_or_404(Trabajo, id=id)
    trabajo.visible = False
    trabajo.save()
    return redirect('lista_trabajos')

def editar_trabajo(request, trabajo_id):
    trabajo = get_object_or_404(Trabajo, id=trabajo_id)
    if request.method == 'POST':
        form = TrabajoForm(request.POST, instance=trabajo)
        if form.is_valid():
            form.save()
            return redirect('trabajos:lista_trabajos')
    else:
        form = TrabajoForm(instance=trabajo)
    return render(request, 'trabajos/editar_trabajo.html', {'form': form, 'trabajo': trabajo})

def pendientes_semana(request):
    hoy = date.today()
    fin_semana = hoy + timedelta(days=7)
    trabajos = Trabajo.objects.filter(estado='Pendiente', fecha__range=[hoy, fin_semana], visible=True)
    return render(request, 'trabajos/pendientes_semana.html', {'trabajos': trabajos})

def detalle_trabajo(request, trabajo_id):
    """
    Muestra los detalles de un trabajo específico,
    incluyendo datos del cliente, planos y cuentas asociadas.
    """
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

# Agregar trabajo
def agregar_trabajo(request):
    if request.method == 'POST':
        form = TrabajoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trabajos/lista_trabajos.html')  
    else:
        form = TrabajoForm()
    return render(request, 'trabajos/agregar_trabajo.html', {'form': form})


