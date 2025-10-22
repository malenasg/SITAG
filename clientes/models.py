from django.db import models

class Organizacion(models.Model):
    nombre = models.CharField(max_length=45)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nombre


from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=45)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    activo = models.BooleanField(default=True) 

    def __str__(self):
        return self.nombre
