from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Cliente, ClienteFisico, ClienteJuridico
from .forms import ClienteBaseForm, ClienteFisicoForm, ClienteJuridicoForm, UbicacionForm

def lista_clientes(request):
    clientes = Cliente.objects.filter(activo=True).select_related(
    'clientefisico',
    'clientejuridico'
)

    return render(request, 'clientes/lista_clientes.html', {
        'clientes': clientes
    })

def agregar_cliente(request):
    tipo = request.POST.get('tipo_cliente', 'fisica')

    if request.method == 'POST':
        cliente_form = ClienteBaseForm(request.POST)
        ubicacion_form = UbicacionForm(request.POST)

        # Elegir el form de detalle según tipo
        if tipo == 'fisica':
            detalle_fisica_form = ClienteFisicoForm(request.POST)
            detalle_juridica_form = ClienteJuridicoForm()
            detalle_form = detalle_fisica_form
        else:
            detalle_fisica_form = ClienteFisicoForm()
            detalle_juridica_form = ClienteJuridicoForm(request.POST)
            detalle_form = detalle_juridica_form

        # Validamos solo los forms correspondientes
        if cliente_form.is_valid() and ubicacion_form.is_valid() and detalle_form.is_valid():
            # Guardar ubicación
            ubicacion = ubicacion_form.save()

            # Guardar cliente
            cliente = cliente_form.save(commit=False)
            cliente.tipo_cliente = tipo
            cliente.ubicacion = ubicacion
            cliente.activo = True
            cliente.save()

            # Guardar detalle según tipo
            detalle_instancia = detalle_form.save(commit=False)
            detalle_instancia.cliente = cliente
            detalle_instancia.save()

            messages.success(request, "Se guardaron los datos correctamente.")
            return redirect('clientes:lista_clientes')
        else:
            messages.error(request, "Revise los campos obligatorios.")

    else:
        cliente_form = ClienteBaseForm()
        ubicacion_form = UbicacionForm()
        detalle_fisica_form = ClienteFisicoForm()
        detalle_juridica_form = ClienteJuridicoForm()

    return render(request, 'clientes/agregar_cliente.html', {
        'cliente_form': cliente_form,
        'ubicacion_form': ubicacion_form,
        'detalle_fisica_form': detalle_fisica_form,
        'detalle_juridica_form': detalle_juridica_form,
        'tipo': tipo
    })

def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    tipo = cliente.tipo_cliente

    # Detalle según tipo
    if tipo == 'fisica':
        detalle_fisica = get_object_or_404(ClienteFisico, cliente=cliente)
        detalle_juridica = None
    else:
        detalle_juridica = get_object_or_404(ClienteJuridico, cliente=cliente)
        detalle_fisica = None

    if request.method == 'POST':
        cliente_form = ClienteBaseForm(request.POST, instance=cliente)
        ubicacion_form = UbicacionForm(request.POST, instance=cliente.ubicacion)

        if tipo == 'fisica':
            detalle_fisica_form = ClienteFisicoForm(request.POST, instance=detalle_fisica)
            detalle_juridica_form = ClienteJuridicoForm()
        else:
            detalle_fisica_form = ClienteFisicoForm()
            detalle_juridica_form = ClienteJuridicoForm(request.POST, instance=detalle_juridica)

        if (
            cliente_form.is_valid()
            and ubicacion_form.is_valid()
            and (
                (tipo == 'fisica' and detalle_fisica_form.is_valid()) or
                (tipo == 'juridica' and detalle_juridica_form.is_valid())
            )
        ):
            cliente_form.save()
            ubicacion_form.save()

            if tipo == 'fisica':
                detalle_fisica_form.save()
            else:
                detalle_juridica_form.save()

            messages.success(request, "Se guardaron los datos correctamente.")
            return redirect('clientes:lista_clientes')

        messages.error(request, "Revisá los campos obligatorios.")

    else:
        cliente_form = ClienteBaseForm(instance=cliente)
        ubicacion_form = UbicacionForm(instance=cliente.ubicacion)
        detalle_fisica_form = ClienteFisicoForm(instance=detalle_fisica)
        detalle_juridica_form = ClienteJuridicoForm(instance=detalle_juridica)

    return render(request, 'clientes/editar_cliente.html', {
        'cliente_form': cliente_form,
        'ubicacion_form': ubicacion_form,
        'detalle_fisica_form': detalle_fisica_form,
        'detalle_juridica_form': detalle_juridica_form,
        'tipo': tipo
    })

def ocultar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    cliente.activo = False
    cliente.save()
    messages.info(request, "Cliente ocultado.")
    return redirect('clientes:lista_clientes')

def mostrar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    cliente.activo = True
    cliente.save()
    messages.success(request, "Cliente reactivado.")
    return redirect('clientes:clientes_ocultos')

def clientes_ocultos(request):
    clientes = Cliente.objects.filter(activo=False)
    return render(request, 'clientes/lista_ocultos.html', {
        'clientes': clientes
    })
