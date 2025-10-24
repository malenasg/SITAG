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
            'fecha_fin',
        ]
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Ej: Mensura Lote 12 - Barrio Norte'}),
            'descripcion': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Detalle del trabajo...'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
        }


class UbicacionForm(forms.ModelForm):
    class Meta:
        model = Ubicacion
        fields = ['calle', 'numero', 'ciudad', 'barrio', 'nomenclatura_catastral']
        widgets = {
            'calle': forms.TextInput(attrs={'placeholder': 'Calle principal'}),
            'numero': forms.NumberInput(),
            'ciudad': forms.TextInput(),
            'barrio': forms.TextInput(),
            'nomenclatura_catastral': forms.TextInput(attrs={'placeholder': 'Ej: Circ. 2, Sec. B, Manz. 5, Parc. 3'}),
        }

