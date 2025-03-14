from django import forms
from .models import Evento
from .models import Paciente

class EventoForm(forms.ModelForm):
    paciente = forms.ModelChoiceField(
        queryset=Paciente.objects.all(),  # Lista de pacientes en el sistema
        empty_label="Seleccione un paciente",
        widget=forms.Select(attrs={'class': 'form-control'})  # Opcional: estilos CSS
    )
    
    class Meta:
        model = Evento
        fields = [
            'paciente',
            'tipo',
            'descripcion',        
            #'fecha'
        ]
        exclude = ['diagnostico']

        labels = {
            'paciente': "Paciente",
            'tipo': "Tipo",
            'descripcion': "Descripcion"
            #'fecha' : "Fecha",
        }