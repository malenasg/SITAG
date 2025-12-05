from django.db import models
from clientes.models import Cliente
from trabajos.models import Trabajo

ESTADO_FACTURA = [
    ('Pagado', 'Pagado'),
    ('Parcial', 'Parcial'),
    ('Adeuda', 'Adeuda'),
]

class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    trabajo = models.ForeignKey(Trabajo, on_delete=models.CASCADE)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    monto_pagado = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    saldo_pendiente = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estado = models.CharField(max_length=20, default='ADEUDA')  # ADEUDA / PARCIAL / PAGADO
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def saldo(self):
        return self.costo_total - self.monto_pagado

    def actualizar_estado(self):
        if self.monto_pagado >= self.costo_total:
            self.estado = 'PAGADO'
        elif self.monto_pagado > 0:
            self.estado = 'PARCIAL'
        else:
            self.estado = 'ADEUDA'
        self.save()

    def __str__(self):
        return f"Factura #{self.id} - {self.cliente}"


class Presupuesto(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    superficie = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=100, default='residencial')
    ubicacion = models.CharField(max_length=255)
    observaciones = models.TextField(blank=True)
    costo_estimado = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    aprobado = models.BooleanField(default=False)
    fecha = models.DateField(auto_now_add=True)

    def calcular_costo(self):
        # Ejemplo: costo = superficie * tarifa por tipo
        tarifa = 1000 if self.tipo.lower() == 'residencial' else 1500
        self.costo_estimado = self.superficie * tarifa
        return self.costo_estimado

class Pago(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField(auto_now_add=True)