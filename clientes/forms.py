from django import forms
from .models import Cliente, ClienteFisico, ClienteJuridico, Ubicacion

class UbicacionForm(forms.ModelForm):
    class Meta:
        model = Ubicacion
        fields = [
            'provincia', 'departamento', 'localidad',
            'calle', 'numero', 'barrio', 'piso', 'codigo_postal'
        ]
        widgets = {
            'departamento': forms.Select(
                attrs={'required': True}
            ),
            'localidad': forms.Select(
                attrs={'required': True}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['departamento'].choices = [
            ('', 'Seleccione un departamento')
        ]
        self.fields['localidad'].choices = [
            ('', 'Seleccione una localidad')
        ]

class ClienteFisicoForm(forms.ModelForm):
    class Meta:
        model = ClienteFisico
        fields = ['nombre', 'apellido', 'cuil']


class ClienteJuridicoForm(forms.ModelForm):
    class Meta:
        model = ClienteJuridico
        fields = ['razon_social', 'cuit']


class ClienteBaseForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['telefono', 'email']
