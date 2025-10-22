from django.shortcuts import render, redirect
from clientes.models import Cliente
from trabajos.models import Trabajo
from datetime import date, timedelta

def inicio(request):
    # Filtros
    cliente_id = request.GET.get('cliente')
    estado = request.GET.get('estado')

    trabajos = Trabajo.objects.filter(visible=True)

    if cliente_id and cliente_id.isdigit():
        trabajos = trabajos.filter(cliente_id=cliente_id)

    if estado and estado != "":
        trabajos = trabajos.filter(estado=estado)

    total_clientes = Cliente.objects.filter(activo=True).count()
    trabajos_activos = Trabajo.objects.filter(estado__in=["En curso", "Pendiente"], visible=True).count()
    pendientes_semana = Trabajo.objects.filter(
        estado="Pendiente",
        fecha_inicio__range=[date.today(), date.today().replace(day=min(date.today().day + 7, 28))]
    ).count()

    clientes = Cliente.objects.filter(activo=True)

    context = {
        "total_clientes": total_clientes,
        "trabajos_activos": trabajos_activos,
        "pendientes_semana": pendientes_semana,
        "trabajos_recientes": trabajos.order_by("-fecha_inicio")[:10],
        "clientes": clientes,
    }
    return render(request, "inicio/inicio.html", context)



# Agregar cliente
def agregar_cliente(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        telefono = request.POST.get("telefono")
        Cliente.objects.create(nombre=nombre, email=email, telefono=telefono)
        return redirect('inicio:inicio')
    return render(request, 'inicio/agregar_cliente.html')


# Trabajos pendientes
def trabajos_pendientes(request):
    hoy = date.today()
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
