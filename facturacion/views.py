from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Presupuesto, Factura, Pago
from trabajos.models import Trabajo
from clientes.models import Cliente
from .forms import PagoForm
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# ----------------- LISTA DE PRESUPUESTOS -----------------
def lista_presupuestos(request):
    presupuestos = Presupuesto.objects.all().order_by('-fecha')
    return render(request, 'facturacion/lista_presupuestos.html', {
        'presupuestos': presupuestos
    })

def nuevo_presupuesto(request, trabajo_id=None):
    trabajo = None
    cliente = None

    if trabajo_id:
        trabajo = get_object_or_404(Trabajo, pk=trabajo_id)
        cliente = trabajo.cliente

    if request.method == "POST":
        # Tomar cliente del formulario o del trabajo
        cliente_id = request.POST.get("cliente") or (cliente.id if cliente else None)
        cliente = get_object_or_404(Cliente, pk=cliente_id)

        presupuesto = Presupuesto(
            cliente=cliente,
            trabajo=trabajo,
            ubicacion=str(trabajo.ubicacion) if trabajo and trabajo.ubicacion else request.POST.get("ubicacion", ""),
            dias_campo=request.POST.get("dias_campo") or 0,
            dias_gabinete=request.POST.get("dias_gabinete") or 0,
            costo_personal=request.POST.get("costo_personal") or 0,
            costo_movilidad=request.POST.get("costo_movilidad") or 0,
            costo_viaticos=request.POST.get("costo_viaticos") or 0,
            costo_materiales=request.POST.get("costo_materiales") or 0,
            costo_desgaste=request.POST.get("costo_desgaste") or 0,
            costo_imprevistos=request.POST.get("costo_imprevistos") or 0,
            gasto_aportes=request.POST.get("gasto_aportes") or 0,
            gasto_sellado=request.POST.get("gasto_sellado") or 0,
            gasto_copias=request.POST.get("gasto_copias") or 0,
            gasto_gestoria=request.POST.get("gasto_gestoria") or 0,
            honorarios_minimos=request.POST.get("honorarios_minimos") or 0,
            honorarios_adicional=request.POST.get("honorarios_adicional") or 0,
            porcentaje_impuestos=request.POST.get("porcentaje_impuestos") or 21,
            observaciones=request.POST.get("observaciones", ""),
            estado=request.POST.get("estado", "pendiente"),
        )
        presupuesto.save()
        messages.success(request, "Presupuesto creado correctamente.")
        return redirect("facturacion:detalle_presupuesto", pk=presupuesto.id)

    return render(request, "facturacion/nuevo_presupuesto.html", {
        "trabajo": trabajo,
        "cliente": cliente
    })

# ----------------- DETALLE PRESUPUESTO -----------------
def detalle_presupuesto(request, pk):
    presupuesto = get_object_or_404(Presupuesto, pk=pk)
    return render(request, 'facturacion/detalle_presupuesto.html', {
        'presupuesto': presupuesto
    })

# ----------------- CAMBIAR ESTADO PRESUPUESTO -----------------
def cambiar_estado_presupuesto(request, pk):
    presupuesto = get_object_or_404(Presupuesto, pk=pk)

    if request.method == "POST":
        nuevo_estado = request.POST.get("estado")
        if nuevo_estado in dict(Presupuesto.ESTADOS):
            presupuesto.estado = nuevo_estado
            presupuesto.save()

            # Crear factura automáticamente si se acepta
            if nuevo_estado == "aceptado":
                Factura.objects.get_or_create(presupuesto=presupuesto)

            messages.success(request, "Estado actualizado correctamente.")

    return redirect("facturacion:detalle_presupuesto", pk=presupuesto.id)

# ----------------- LISTA DE FACTURAS -----------------
def lista_facturas(request):
    facturas = Factura.objects.all().order_by('-fecha')
    return render(request, 'facturacion/lista_facturas.html', {
        'facturas': facturas
    })

# ----------------- DETALLE FACTURA -----------------
def detalle_factura(request, pk):
    factura = get_object_or_404(Factura, pk=pk)
    pagos = factura.pagos.all()
    return render(request, 'facturacion/detalle_factura.html', {
        'factura': factura,
        'pagos': pagos
    })

# ----------------- REGISTRAR PAGO -----------------
def registrar_pago(request, factura_id):
    factura = get_object_or_404(Factura, pk=factura_id)

    if request.method == "POST":
        form = PagoForm(request.POST)
        if form.is_valid():
            pago = form.save(commit=False)
            pago.factura = factura
            pago.save()
            messages.success(request, "Pago registrado correctamente.")
            return redirect("facturacion:detalle_factura", pk=factura.id)
    else:
        form = PagoForm()

    return render(request, "facturacion/registrar_pago.html", {
        "form": form,
        "factura": factura
    })

# ----------------- GENERAR PDF -----------------
def factura_pdf(request, pk):
    factura = get_object_or_404(Factura, pk=pk)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="factura_{factura.id}.pdf"'

    p = canvas.Canvas(response, pagesize=A4)
    width, height = A4
    y = height - 40

    # --- Encabezado ---
    p.setFont("Helvetica-Bold", 16)
    p.drawString(40, y, "FACTURA")
    y -= 30

    p.setFont("Helvetica", 10)
    p.drawString(40, y, f"Factura Nº: {factura.id}")
    y -= 15
    p.drawString(40, y, f"Fecha: {factura.fecha}")
    y -= 30

    # --- Cliente ---
    p.setFont("Helvetica-Bold", 11)
    p.drawString(40, y, "Cliente")
    y -= 15
    p.setFont("Helvetica", 10)
    p.drawString(40, y, f"{factura.presupuesto.trabajo.cliente.nombre}")
    y -= 30

    # --- Trabajo ---
    p.setFont("Helvetica-Bold", 11)
    p.drawString(40, y, "Detalle del trabajo")
    y -= 15
    trabajo = factura.presupuesto.trabajo.titulo if factura.presupuesto.trabajo else "No especificado"
    p.setFont("Helvetica", 10)
    p.drawString(40, y, trabajo)
    y -= 30

    # --- Totales ---
    p.setFont("Helvetica-Bold", 11)
    p.drawString(40, y, "Totales")
    y -= 20

    p.setFont("Helvetica", 10)
    p.drawString(40, y, f"Monto total: $ {factura.monto_total:.2f}")
    y -= 15
    p.drawString(40, y, f"Monto pagado: $ {factura.monto_pagado:.2f}")
    y -= 15
    p.drawString(40, y, f"Saldo: $ {factura.saldo:.2f}")
    y -= 30

    estado = "PAGADA" if factura.pagada else "PENDIENTE"
    p.setFont("Helvetica-Bold", 12)
    p.drawString(40, y, f"Estado: {estado}")

    # --- Pie ---
    p.setFont("Helvetica", 8)
    p.drawString(40, 40, "Documento generado por SITAG – Sistema de Agrimensura")

    p.showPage()
    p.save()
    return response
