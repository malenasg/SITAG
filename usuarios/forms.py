from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from .models import Usuario


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Usuario",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

Usuario = get_user_model()

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'username', 'email', 'rol']

        labels = {
            'first_name': 'Nombre completo',
            'username': 'Usuario',
            'email': 'Correo',
            'rol': 'Rol',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'rol': forms.Select(attrs={'class': 'form-control'}),
        }

from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    error_messages = {
        "invalid_login": (
            "Usuario/contraseña incorrectos. Inténtelo de nuevo."
        ),
        "inactive": (
            "Esta cuenta está inactiva. Comuníquese con administración."
        ),
    }
