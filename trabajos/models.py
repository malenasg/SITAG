from django.db import models
from clientes.models import Cliente
from usuarios.models import Usuario

class Ubicacion(models.Model):
    numero = models.CharField(max_length=4, blank=True, null=True)
    calle = models.CharField(max_length=50, blank=True, null=True)
    ciudad = models.CharField(max_length=25, blank=True, null=True)
    barrio = models.CharField(max_length=50, blank=True, null=True)
    departamento = models.CharField(max_length=35, blank=True, null=True)
    localidad = models.CharField(max_length=35, blank=True, null=True)
    nomenclatura_catastral = models.CharField(max_length=20, blank=True, null=True)
    coordenadas = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        calle = self.calle or ''
        numero = f" {self.numero}" if self.numero else ''
        ciudad = f" - {self.ciudad}" if self.ciudad else ''
        return f"{calle}{numero}{ciudad}".strip()

class Trabajo(models.Model):
    TIPO_TRABAJO_CHOICES = [
        ('levantamiento_planimetrico', 'Levantamiento planimétrico'),
        ('levantamiento_altimetrico', 'Levantamiento altimétrico'),
        ('levantamiento_topografico_integral', 'Levantamiento topográfico integral'),
        ('levantamiento_gps_gnss', 'Levantamiento con GPS/GNSS'),
        ('levantamiento_drones', 'Levantamiento con drones/UAV'),
        ('levantamiento_estacion_total', 'Levantamiento con estación total'),
        ('mensura_urbana', 'Mensura de parcelas urbanas'),
        ('mensura_rural', 'Mensura de parcelas rurales'),
        ('subdivision_loteos', 'Subdivisión de terrenos'),
        ('unificacion_parcelas', 'Unificación de parcelas'),
        ('relevamiento_limites', 'Relevamiento de límites'),
        ('actualizacion_catastral', 'Actualización catastral'),
        ('determinacion_areas', 'Determinación de superficies'),
        ('nivelacion_obras', 'Nivelación de obras'),
        ('trazado_replanteo', 'Trazado y replanteo'),
        ('control_deformaciones', 'Control de deformaciones'),
        ('levantamiento_as_built', 'Levantamiento As-built'),
    ]

    ESTADO_CHOICES = [
        ("Pendiente", "Pendiente"),
        ("En curso", "En curso"),
        ("Finalizado", "Finalizado")
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='trabajos')
    descripcion = models.TextField(max_length=100, blank=True)
    tipo_trabajo = models.CharField(max_length=50, choices=TIPO_TRABAJO_CHOICES)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default="Pendiente")
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.SET_NULL, null=True, blank=True)
    responsable = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def titulo(self):
        return self.get_tipo_trabajo_display()

    def __str__(self):
        return self.titulo

class Plano(models.Model):
    fecha = models.DateTimeField()
    descripcion = models.CharField(max_length=255)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE, related_name='planos')
    trabajo = models.ForeignKey(Trabajo, on_delete=models.CASCADE, related_name='planos')
    archivo = models.FileField(upload_to='planos/', null=True, blank=True)

    def __str__(self):
        return f"Plano {self.id} - {self.trabajo.titulo or self.trabajo.descripcion[:20]}"
