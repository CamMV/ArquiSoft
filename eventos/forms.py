from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = [
            'paciente',
            'diagnostico',
            'tipo',
            'descripcion',        
            #'fecha'
        ]
        
        labels = {
            'paciente': "Paciente",
            'diagnostico': "Diagnostico",
            'tipo': "Tipo",
            'descripcion': "Descripcion"
            #'fecha' : "Fecha",
        }