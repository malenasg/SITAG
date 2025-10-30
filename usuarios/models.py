from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    rol = models.CharField(
        max_length=20, 
        choices=[('administrador', 'Administrador'), ('empleado', 'Empleado')]
    )

    @property
    def activo(self):
        return self.is_active
