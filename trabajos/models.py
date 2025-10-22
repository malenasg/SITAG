from django.db import models
from clientes.models import Cliente
from usuarios.models import Usuario

class Ubicacion(models.Model):
    numero = models.IntegerField(blank=True, null=True)
    calle = models.CharField(max_length=45, blank=True, null=True)
    ciudad = models.CharField(max_length=45, blank=True, null=True)
    barrio = models.CharField(max_length=45, blank=True, null=True)
    nomenclatura_catastral = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.calle} {self.numero or ''} - {self.ciudad or ''}".strip()


class Trabajo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha_inicio = models.DateField(auto_now_add=True)
    estado = models.CharField(
        max_length=20,
        choices=[
            ("Pendiente", "Pendiente"),
            ("En curso", "En curso"),
            ("Finalizado", "Finalizado")
        ],
        default="Pendiente"
    )
    visible = models.BooleanField(default=True)
    

    def __str__(self):
        return f"{self.descripcion} - {self.cliente.nombre}"



class Plano(models.Model):
    fecha = models.DateTimeField()
    descripcion = models.CharField(max_length=255)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    trabajo = models.ForeignKey(Trabajo, on_delete=models.CASCADE)

    def __str__(self):
        return f"Plano {self.id} - {self.trabajo.titulo}"


class Cuenta(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('pagado', 'Pagado'),
        ('parcial', 'Parcial'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    trabajo = models.ForeignKey(Trabajo, on_delete=models.CASCADE)
    costo_total = models.DecimalField(max_digits=10, decimal_places=2)
    monto_pagado = models.DecimalField(max_digits=10, decimal_places=2)
    saldo_pendiente = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=10, choices=ESTADOS, default='pendiente')
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Cuenta #{self.id} - {self.cliente.nombre}"
