from django import forms
from .models import Factura, Pago, Presupuesto

# ----------------- Form Factura -----------------
class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['trabajo', 'cliente', 'monto_total', 'monto_pagado', 'estado']

# ----------------- Form Pago -----------------
class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ['factura', 'monto']

# ----------------- Form Presupuesto -----------------
class PresupuestoForm(forms.ModelForm):
    class Meta:
        model = Presupuesto
        fields = ['cliente', 'titulo', 'superficie', 'tipo', 'ubicacion', 'observaciones', 'costo_estimado', 'aprobado']
