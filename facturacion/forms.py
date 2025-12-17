from django import forms
from .models import Factura, Presupuesto, Pago
from trabajos.models import Trabajo

# ======================================================
#                   FORM FACTURA
# ======================================================
class FacturaForm(forms.ModelForm):
    presupuesto = forms.ModelChoiceField(
        queryset=Presupuesto.objects.filter(factura__isnull=True),
        empty_label="Seleccione un presupuesto"
    )

    class Meta:
        model = Factura
        fields = ['presupuesto', 'monto_pagado', 'pagada']
        widgets = {
            'monto_pagado': forms.NumberInput(attrs={'step': '0.01', 'min': 0}),
        }

    def clean(self):
        cleaned = super().clean()
        presupuesto = cleaned.get('presupuesto')
        monto_pagado = cleaned.get('monto_pagado')

        if presupuesto and monto_pagado is not None:
            if monto_pagado > presupuesto.total:
                self.add_error('monto_pagado', 'El monto pagado no puede superar el total del presupuesto.')
            cleaned['pagada'] = (monto_pagado >= presupuesto.total)

        return cleaned


# ======================================================
#                 FORM PRESUPUESTO
# ======================================================
class PresupuestoForm(forms.ModelForm):
    class Meta:
        model = Presupuesto
        fields = [
            'trabajo', 'dias_campo', 'dias_gabinete',

            # ----- Costos directos de campo -----
            'costo_personal', 'costo_movilidad', 'costo_viaticos',
            'costo_materiales', 'costo_desgaste', 'costo_imprevistos',

            # ----- Gastos de gestión -----
            'gasto_aportes', 'gasto_sellado', 'gasto_copias', 'gasto_gestoria',

            # ----- Honorarios -----
            'honorarios_minimos', 'honorarios_adicional',

            # ----- Impuestos y otros -----
            'porcentaje_impuestos', 'observaciones', 'estado'
        ]

        widgets = {
            # DATOS DE TRABAJO
            'dias_campo': forms.NumberInput(attrs={'min': 0}),
            'dias_gabinete': forms.NumberInput(attrs={'min': 0}),

            # COSTOS CAMPO
            'costo_personal': forms.NumberInput(attrs={'step': '0.01', 'min': 0}),
            'costo_movilidad': forms.NumberInput(attrs={'step': '0.01', 'min': 0}),
            'costo_viaticos': forms.NumberInput(attrs={'step': '0.01', 'min': 0}),
            'costo_materiales': forms.NumberInput(attrs={'step': '0.01', 'min': 0}),
            'costo_desgaste': forms.NumberInput(attrs={'step': '0.01', 'min': 0}),
            'costo_imprevistos': forms.NumberInput(attrs={'step': '0.01', 'min': 0}),

            # GESTIÓN
            'gasto_aportes': forms.NumberInput(attrs={'step': '0.01', 'min': 0}),
            'gasto_sellado': forms.NumberInput(attrs={'step': '0.01', 'min': 0}),
            'gasto_copias': forms.NumberInput(attrs={'step': '0.01', 'min': 0}),
            'gasto_gestoria': forms.NumberInput(attrs={'step': '0.01', 'min': 0}),

            # HONORARIOS
            'honorarios_minimos': forms.NumberInput(attrs={'step': '0.01', 'min': 0}),
            'honorarios_adicional': forms.NumberInput(attrs={'step': '0.01', 'min': 0}),

            # IMPUESTOS
            'porcentaje_impuestos': forms.NumberInput(attrs={'step': '0.01', 'min': 0}),

            # OTROS
            'observaciones': forms.Textarea(attrs={'rows': 3}),
        }

    def clean(self):
        cleaned = super().clean()
        numeric_fields = [
            'costo_personal','costo_movilidad','costo_viaticos','costo_materiales',
            'costo_desgaste','costo_imprevistos',
            'gasto_aportes','gasto_sellado','gasto_copias','gasto_gestoria',
            'honorarios_minimos','honorarios_adicional',
            'porcentaje_impuestos',
            'dias_campo','dias_gabinete'
        ]
        for field in numeric_fields:
            value = cleaned.get(field)
            if value is not None and float(value) < 0:
                self.add_error(field, 'El valor no puede ser negativo.')
        return cleaned


# ======================================================
#                 FORM PAGO
# ======================================================
class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ['monto', 'fecha', 'metodo_pago']
