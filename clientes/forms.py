from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        exclude = ['activo']

    def clean(self):
        cleaned_data = super().clean()
        tipo = cleaned_data.get("tipo_cliente")

        if tipo == "fisica":
            if not cleaned_data.get("nombre") or not cleaned_data.get("apellido") or not cleaned_data.get("cuil"):
                raise forms.ValidationError("Para persona física se requieren nombre, apellido y CUIL")
        elif tipo == "juridica":
            if not cleaned_data.get("razon_social") or not cleaned_data.get("cuil"):
                raise forms.ValidationError("Para persona jurídica se requieren razón social y CUIT")
        return cleaned_data
