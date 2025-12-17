from django.shortcuts import render, redirect
from clientes.models import Cliente
from trabajos.models import Trabajo
from datetime import datetime, timedelta
import json
from django.db.models import Count
from usuarios.models import Usuario


def inicio(request):
    # --- 1️⃣ Trabajos filtrados ---
    trabajos = Trabajo.objects.select_related(
        'cliente', 'cliente__clientefisico', 'cliente__clientejuridico'
    )

    # Filtros GET
    estado = request.GET.get('estado')
    if estado:
        trabajos = trabajos.filter(estado=estado)

    tipo_cliente = request.GET.get('tipo_cliente')
    if tipo_cliente:
        trabajos = trabajos.filter(cliente__tipo_cliente=tipo_cliente)

    responsable_id = request.GET.get('responsable')
    if responsable_id:
        trabajos = trabajos.filter(responsable_id=responsable_id)

    # --- 2️⃣ Totales ---
    total_clientes = Cliente.objects.count()
    trabajos_activos = trabajos.filter(estado="Activo").count()
    trabajos_pendientes = trabajos.filter(estado="Pendiente").count()

    # --- 3️⃣ Estadísticas para gráficos ---
    estados_qs = trabajos.values("estado").annotate(cantidad=Count("id"))
    estados_data = {
        "labels": [e["estado"] for e in estados_qs],
        "values": [e["cantidad"] for e in estados_qs],
    }

    mensual_qs = (
        trabajos
        .extra(select={"mes": "MONTH(fecha_inicio)"})
        .values("mes")
        .annotate(cantidad=Count("id"))
        .order_by("mes")
    )
    mensual_data = {
        "labels": [m["mes"] for m in mensual_qs],
        "values": [m["cantidad"] for m in mensual_qs],
    }

    # --- 4️⃣ Datos para filtros ---
    estados = Trabajo.objects.values_list('estado', flat=True).distinct()
    usuarios = Usuario.objects.all()

    # --- 5️⃣ Contexto final ---
    context = {
        "trabajos": trabajos,
        "total_clientes": total_clientes,
        "trabajos_activos": trabajos_activos,
        "trabajos_pendientes": trabajos_pendientes,
        "estados_data": json.dumps(estados_data),
        "mensual_data": json.dumps(mensual_data),
        "estados": estados,
        "usuarios": usuarios,
    }

    return render(request, "inicio/inicio.html", context)


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
