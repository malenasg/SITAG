from django import forms
from django.core.validators import RegexValidator
from .models import Cliente

cuil_validator = RegexValidator(
    regex=r'^\d{2}-\d{8}-\d{1}$',
    message='El CUIL/CUIT debe tener el formato XX-XXXXXXXX-X'
)

class ClienteForm(forms.ModelForm):
    cuil = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '20-12345678-9'})
    )


    class Meta:
        model = Cliente
        fields = '__all__'
        exclude = ['activo']

def clean(self):
    cleaned_data = super().clean()

    tipo = cleaned_data.get("tipo_cliente")
    cuil = cleaned_data.get("cuil")

    if tipo == "fisica":
        if not cleaned_data.get("nombre"):
            self.add_error('nombre', 'El nombre es obligatorio')
        if not cleaned_data.get("apellido"):
            self.add_error('apellido', 'El apellido es obligatorio')
        if not cuil:
            self.add_error('cuil', 'El CUIL es obligatorio')
        else:
            if not re.match(r'^\d{2}-\d{8}-\d{1}$', cuil):
                self.add_error('cuil', 'Formato incorrecto. Ejemplo: 20-12345678-9')

    if tipo == "juridica":
        if not cleaned_data.get("razon_social"):
            self.add_error('razon_social', 'La razón social es obligatoria')
        if not cuil:
            self.add_error('cuil', 'El CUIT es obligatorio')
        else:
            if not re.match(r'^\d{2}-\d{8}-\d{1}$', cuil):
                self.add_error('cuil', 'Formato incorrecto. Ejemplo: 30-12345678-9')

    return cleaned_data
