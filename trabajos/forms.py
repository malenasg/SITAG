from django import forms
from .models import Trabajo, Ubicacion

class TrabajoForm(forms.ModelForm):
    class Meta:
        model = Trabajo
        fields = [
            'cliente',
            'titulo',
            'descripcion',
            'estado',
            'visible',
            'responsable',
            'fecha_inicio',
        ]
        widgets = {
            'titulo': forms.TextInput(),
            'descripcion': forms.Textarea(),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
        }


class UbicacionForm(forms.ModelForm):
    class Meta:
        model = Ubicacion
        fields = ['calle', 'numero', 'ciudad', 'barrio', 'nomenclatura_catastral']
        widgets = {
            'calle': forms.TextInput(),
            'numero': forms.NumberInput(),
            'ciudad': forms.TextInput(),
            'barrio': forms.TextInput(),
            'nomenclatura_catastral': forms.TextInput(),
        }

