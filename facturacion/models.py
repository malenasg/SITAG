from django.db import models
from trabajos.models import Trabajo
from decimal import Decimal
from datetime import date
from django.db import transaction
from django.db.models import Sum
from decimal import Decimal

class Presupuesto(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('aceptado', 'Aceptado'),
        ('rechazado', 'Rechazado'),
    ]

    trabajo = models.OneToOneField(
        Trabajo,
        on_delete=models.CASCADE,
        related_name='presupuesto'
    )

    
    dias_campo = models.PositiveIntegerField(default=0)
    dias_gabinete = models.PositiveIntegerField(default=0)

    # Costos directos
    costo_personal = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    costo_movilidad = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    costo_viaticos = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    costo_materiales = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    costo_desgaste = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    costo_imprevistos = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    # Gastos de gabinete
    gasto_aportes = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    gasto_sellado = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    gasto_copias = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    gasto_gestoria = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    # Honorarios
    honorarios_minimos = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    honorarios_adicional = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    # Subtotales y totales
    subtotal_gastos_campo = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    subtotal_gastos_gestion = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    subtotal_honorarios = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    subtotal = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    impuestos = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    porcentaje_impuestos = models.DecimalField(max_digits=5, decimal_places=2, default=21.00)

    observaciones = models.TextField(blank=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    fecha = models.DateField(default=date.today)

    # ---------- Cálculos ----------
    def calcular_totales(self):
        def d(value): return Decimal(value or 0)

        subtotal_campo = (
            d(self.costo_personal) + d(self.costo_movilidad) +
            d(self.costo_viaticos) + d(self.costo_materiales) +
            d(self.costo_desgaste) + d(self.costo_imprevistos)
        )
        subtotal_gestion = (
            d(self.gasto_aportes) + d(self.gasto_sellado) +
            d(self.gasto_copias) + d(self.gasto_gestoria)
        )
        subtotal_honorarios = d(self.honorarios_minimos) + d(self.honorarios_adicional)
        subtotal = subtotal_campo + subtotal_gestion + subtotal_honorarios
        impuestos = (subtotal * d(self.porcentaje_impuestos) / Decimal(100)).quantize(Decimal("0.01"))
        total = (subtotal + impuestos).quantize(Decimal("0.01"))

        self.subtotal_gastos_campo = subtotal_campo
        self.subtotal_gastos_gestion = subtotal_gestion
        self.subtotal_honorarios = subtotal_honorarios
        self.subtotal = subtotal
        self.impuestos = impuestos
        self.total = total

    def save(self, *args, **kwargs):
        self.calcular_totales()
        super().save(*args, **kwargs)

    def __str__(self):
        t = self.trabajo.titulo if self.trabajo else "Sin trabajo"
        return f"Presupuesto {self.id} - {t}"


# ===========================
#           FACTURA
# ===========================
class Factura(models.Model):
    presupuesto = models.OneToOneField(Presupuesto, on_delete=models.CASCADE, related_name="factura")
    pagada = models.BooleanField(default=False)
    monto_pagado = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    fecha = models.DateField(default=date.today)
    metodo_pago = models.CharField(max_length=50, null=True, blank=True)

    @property
    def monto_total(self):
        return self.presupuesto.total

    @property
    def saldo(self):
        return (self.monto_total - self.monto_pagado).quantize(Decimal("0.01"))

    def actualizar_pagada(self, save=True):
        self.pagada = self.monto_pagado >= self.monto_total
        if save:
            self.save(update_fields=["pagada", "monto_pagado"])

    def __str__(self):
        return f"Factura {self.id} - Presupuesto {self.presupuesto.id}"

class Pago(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, related_name='pagos')
    fecha = models.DateField(default=date.today)
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    metodo_pago = models.CharField(max_length=50, null=True, blank=True)

    def save(self, *args, **kwargs):
        with transaction.atomic():
            super().save(*args, **kwargs)

            total_pagado = (
                self.factura.pagos.aggregate(total=Sum('monto'))['total']
                or Decimal('0')
            )

            self.factura.monto_pagado = total_pagado
            self.factura.actualizar_pagada(save=True)

    def __str__(self):
        return f"Pago {self.id} - Factura {self.factura.id}"
