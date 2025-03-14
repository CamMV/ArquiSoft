from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'edad', 'historia_clinica']
        labels = {
            'nombre': 'Nombre del paciente',
            'edad': 'Edad del paciente',
            'historia_clinica': 'Historia clínica del paciente'
        }