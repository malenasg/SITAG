from django import forms
from .models import Trabajo, Ubicacion, Cliente

class TrabajoForm(forms.ModelForm):

    TIPO_TRABAJO_CHOICES = [
        ('Levantamientos Topográficos', [
            ('levantamiento_planimetrico', 'Levantamiento planimétrico'),
            ('levantamiento_altimetrico', 'Levantamiento altimétrico'),
            ('levantamiento_topografico_integral', 'Levantamiento topográfico integral'),
            ('levantamiento_gps_gnss', 'Levantamiento con GPS/GNSS'),
            ('levantamiento_drones', 'Levantamiento con drones/UAV'),
            ('levantamiento_estacion_total', 'Levantamiento con estación total'),
        ]),
        ('Estudios Catastrales y Parcelarios', [
            ('mensura_urbana', 'Mensura de parcelas urbanas'),
            ('mensura_rural', 'Mensura de parcelas rurales'),
            ('subdivision_loteos', 'Subdivisión de terrenos (loteos)'),
            ('unificacion_parcelas', 'Unificación de parcelas'),
            ('relevamiento_limites', 'Relevamiento de límites y deslindes'),
            ('actualizacion_catastral', 'Actualización catastral'),
            ('determinacion_areas', 'Determinación de superficies y áreas'),
        ]),
        ('Ingeniería y Construcción', [
            ('nivelacion_obras', 'Nivelación de obras'),
            ('trazado_replanteo', 'Trazado y replanteo de obras'),
            ('control_deformaciones', 'Control de deformaciones estructurales'),
            ('levantamiento_as_built', 'Levantamiento As-built'),
        ]),
    ]

    tipo_trabajo = forms.ChoiceField(
        choices=TIPO_TRABAJO_CHOICES,
        widget=forms.Select()
    )

    class Meta:
        model = Trabajo
        fields = [
            'cliente',
            'descripcion',
            'tipo_trabajo',
            'estado',
            'responsable',
            'fecha_inicio',
            'fecha_fin',
        ]
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
            'estado': forms.Select(),
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cliente'].queryset = Cliente.objects.filter(activo=True)
        for field in self.fields.values():
            if isinstance(field, forms.ModelChoiceField):
                field.empty_label = "Seleccione una opción"

class UbicacionForm(forms.ModelForm):
    class Meta:
        model = Ubicacion
        fields = [
            'calle', 'numero', 'ciudad', 'barrio',
            'departamento', 'localidad',
            'nomenclatura_catastral', 'coordenadas'
        ]
        widgets = {
            'calle': forms.TextInput(),
            'numero': forms.NumberInput(),
            'ciudad': forms.TextInput(),
            'barrio': forms.TextInput(),

            # 🔥 CLAVE
            'departamento': forms.TextInput(attrs={
                'id': 'id_departamento',
                'autocomplete': 'off',
                'placeholder': 'Departamento'
            }),
            'localidad': forms.TextInput(attrs={
                'id': 'id_localidad',
                'autocomplete': 'off',
                'placeholder': 'Localidad'
            }),

            'nomenclatura_catastral': forms.TextInput(),
            'coordenadas': forms.TextInput(attrs={
                'placeholder': '-27.4513, -58.9864'
            }),
        }
