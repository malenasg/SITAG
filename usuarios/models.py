from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    ROLES = [
        ('administrador', 'Administrador'),
        ('empleado', 'Empleado'),
    ]

    rol = models.CharField(max_length=20, choices=ROLES, default='empleado')

    def __str__(self):
        return f"{self.username} ({self.get_rol_display()})"
