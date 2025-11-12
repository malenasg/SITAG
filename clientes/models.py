from django.db import models

class Cliente(models.Model):
    TIPO_CHOICES = [
        ('fisica', 'Persona Física'),
        ('juridica', 'Persona Jurídica'),
    ]

    tipo_cliente = models.CharField(max_length=10, choices=TIPO_CHOICES, default='fisica')
    nombre = models.CharField(max_length=45, blank=True, null=True)
    apellido = models.CharField(max_length=45, blank=True, null=True)
    razon_social = models.CharField(max_length=100, blank=True, null=True)
    cuil = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    localidad = models.CharField(max_length=100, blank=True, null=True)
    provincia = models.CharField(max_length=100, blank=True, null=True)
    calle = models.CharField(max_length=100, blank=True, null=True)
    numero = models.CharField(max_length=10, blank=True, null=True)
    barrio = models.CharField(max_length=100, blank=True, null=True)
    piso = models.CharField(max_length=10, blank=True, null=True)
    departamento = models.CharField(max_length=10, blank=True, null=True)
    codigo_postal = models.CharField(max_length=10, blank=True, null=True)

    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.razon_social or f"{self.nombre} {self.apellido}"