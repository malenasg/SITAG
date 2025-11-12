from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Usuario", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

ROLES = [
    ('administrador', 'Administrador'),
    ('empleado', 'Empleado'),
]

from django.contrib.auth.models import AbstractUser
from django.db import models

ROLES = [
    ('administrador', 'Administrador'),
    ('empleado', 'Empleado'),
]

class Usuario(AbstractUser):
    dni = models.CharField(max_length=20, unique=True)
    rol = models.CharField(max_length=20, choices=ROLES, default='empleado')

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"
