from django.shortcuts import render, redirect
from clientes.models import Cliente
from trabajos.models import Trabajo
from datetime import datetime, timedelta

def inicio(request):

    total_clientes = Cliente.objects.count()
    trabajos_activos = Trabajo.objects.filter(estado='Activo').count()

    semana_atras = datetime.now() - timedelta(days=7)
    trabajos_pendientes = Trabajo.objects.filter(estado='Pendiente', fecha_inicio__gte=semana_atras).count()

    localidades = Cliente.objects.values_list('localidad', flat=True).distinct()
    estados = Trabajo.objects.values_list('estado', flat=True).distinct()
    trabajos = Trabajo.objects.all()

    orden = request.GET.get('orden')
    if orden in ['fecha_inicio', 'titulo']:
        trabajos = trabajos.order_by(orden)

    localidad = request.GET.get('localidad')
    if localidad:
        trabajos = trabajos.filter(cliente__localidad=localidad)

    estado = request.GET.get('estado')
    if estado:
        trabajos = trabajos.filter(estado=estado)

    context = {
        'total_clientes': total_clientes,
        'trabajos_activos': trabajos_activos,
        'trabajos_pendientes': trabajos_pendientes,
        'localidades': localidades,
        'estados': estados,
        'trabajos': trabajos,
    }
    return render(request, 'inicio/inicio.html', context)

# Trabajos pendientes
def trabajos_pendientes(request):
    hoy = datetime.today()
    inicio_semana = hoy - timedelta(days=hoy.weekday()) 
    fin_semana = inicio_semana + timedelta(days=6)        

    pendientes = Trabajo.objects.filter(
        estado='Pendiente',
        fecha_inicio__range=[inicio_semana, fin_semana]
    )

    context = {
        'pendientes': pendientes,
        'inicio_semana': inicio_semana,
        'fin_semana': fin_semana
    }
    return render(request, 'inicio/pendientes.html', context)
