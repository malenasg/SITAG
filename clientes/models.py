from django.db import models

# ===========================
# UBICACIÓN
# ===========================
class Ubicacion(models.Model):
    provincia = models.CharField(max_length=10)
    departamento = models.CharField(max_length=30)
    localidad = models.CharField(max_length=50)
    calle = models.CharField(max_length=30)
    numero = models.CharField(max_length=5)
    barrio = models.CharField(max_length=30, blank=True, null=True)
    piso = models.CharField(max_length=4, blank=True, null=True)
    codigo_postal = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return f"{self.calle} {self.numero} - {self.localidad}"


# ===========================
# CLIENTE BASE
# ===========================
class Cliente(models.Model):
    TIPO_CHOICES = [
        ('fisica', 'Persona Física'),
        ('juridica', 'Persona Jurídica'),
    ]

    tipo_cliente = models.CharField(max_length=10, choices=TIPO_CHOICES)
    telefono = models.CharField(max_length=10)
    email = models.EmailField(max_length=30)
    activo = models.BooleanField(default=True)

    ubicacion = models.OneToOneField(
        Ubicacion,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        if self.tipo_cliente == 'juridica' and hasattr(self, 'clientejuridico'):
            return self.clientejuridico.razon_social
        if self.tipo_cliente == 'fisica' and hasattr(self, 'clientefisico'):
            return f"{self.clientefisico.nombre} {self.clientefisico.apellido}"
        return "Cliente"


# ===========================
# CLIENTE FÍSICO
# ===========================
class ClienteFisico(models.Model):
    cliente = models.OneToOneField(
        Cliente,
        on_delete=models.CASCADE,
        related_name='clientefisico'
    )
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=20)
    cuil = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# ===========================
# CLIENTE JURÍDICO
# ===========================
class ClienteJuridico(models.Model):
    cliente = models.OneToOneField(
        Cliente,
        on_delete=models.CASCADE,
        related_name='clientejuridico'
    )
    razon_social = models.CharField(max_length=30)
    cuit = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.razon_social
