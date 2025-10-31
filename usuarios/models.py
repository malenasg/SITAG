from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    ROLES = [
        ('administrador', 'Administrador'),
        ('empleado', 'Empleado'),
    ]
    rol = models.CharField(max_length=20, choices=ROLES, default='empleado')
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.username
