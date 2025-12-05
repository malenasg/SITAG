from django.shortcuts import render, redirect, get_object_or_404
from .models import Factura, Pago, Presupuesto
from .forms import FacturaForm, PagoForm, PresupuestoForm

# ----------------- Facturas -----------------
def lista_facturas(request):
    facturas = Factura.objects.all()
    return render(request, 'facturacion/lista_facturas.html', {'facturas': facturas})

def nueva_factura(request):
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('facturacion:lista_facturas')
    else:
        form = FacturaForm()
    return render(request, 'facturacion/nueva_factura.html', {'form': form})

def editar_factura(request, pk):
    factura = get_object_or_404(Factura, pk=pk)
    if request.method == 'POST':
        form = FacturaForm(request.POST, instance=factura)
        if form.is_valid():
            form.save()
            return redirect('facturacion:lista_facturas')
    else:
        form = FacturaForm(instance=factura)
    return render(request, 'facturacion/editar_factura.html', {'form': form, 'factura': factura})

# ----------------- Pagos -----------------
def lista_pagos(request):
    pagos = Pago.objects.all()
    return render(request, 'facturacion/lista_pagos.html', {'pagos': pagos})

def nuevo_pago(request):
    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            pago = form.save()
            # Actualizar monto_pagado en la factura
            factura = pago.factura
            factura.monto_pagado += pago.monto
            factura.actualizar_estado()
            return redirect('facturacion:lista_pagos')
    else:
        form = PagoForm()
    return render(request, 'facturacion/nuevo_pago.html', {'form': form})

# ----------------- Presupuestos -----------------
def lista_presupuestos(request):
    presupuestos = Presupuesto.objects.all()
    return render(request, 'facturacion/lista_presupuestos.html', {'presupuestos': presupuestos})

def nuevo_presupuesto(request):
    if request.method == 'POST':
        form = PresupuestoForm(request.POST)
        if form.is_valid():
            presupuesto = form.save()
            presupuesto.calcular_costo()
            presupuesto.save()
            return redirect('facturacion:lista_presupuestos')
    else:
        form = PresupuestoForm()
    return render(request, 'facturacion/nuevo_presupuesto.html', {'form': form})
