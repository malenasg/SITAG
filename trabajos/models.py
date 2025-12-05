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
        calle = self.calle or ''
        numero = f" {self.numero}" if self.numero else ''
        ciudad = f" - {self.ciudad}" if self.ciudad else ''
        return f"{calle}{numero}{ciudad}".strip()


class Trabajo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='trabajos')
    titulo = models.CharField(max_length=250, blank=True)   
    descripcion = models.TextField(max_length=200)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)     
    estado = models.CharField(max_length=20,
        choices=[
            ("Pendiente", "Pendiente"),
            ("En curso", "En curso"),
            ("Finalizado", "Finalizado")
        ],
        default="Pendiente"
    )
    visible = models.BooleanField(default=True)

    costo_total = models.DecimalField(max_digits=12, decimal_places=2)
    
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.SET_NULL, null=True, blank=True, related_name='trabajos')
    responsable = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, related_name='trabajos_responsable')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        titulo = self.titulo or (self.descripcion[:30] + '...')
        return f"{titulo} - {self.cliente.nombre}"
    
    @property
    def pagado_total(self):
        return sum(p.monto for p in self.pagos.all())

    @property
    def saldo(self):
        factura = getattr(self, 'factura', None)
        if factura:
            return factura.saldo
        return self.costo_total  # Si no hay factura creada

    @property
    def estado_facturacion(self):
        factura = getattr(self, 'factura', None)
        if factura:
            return factura.estado
        return "SIN FACTURA"


class Plano(models.Model):
    fecha = models.DateTimeField()
    descripcion = models.CharField(max_length=255)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE, related_name='planos')
    trabajo = models.ForeignKey(Trabajo, on_delete=models.CASCADE, related_name='planos')
    archivo = models.FileField(upload_to='planos/', null=True, blank=True)

    def __str__(self):
        return f"Plano {self.id} - {self.trabajo.titulo or self.trabajo.descripcion[:20]}"
