from django import forms
from .models import Trabajo

class TrabajoForm(forms.ModelForm):
    class Meta:
        model = Trabajo
        fields = ['descripcion', 'estado', 'visible']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
            'estado': forms.Select(),
        }
