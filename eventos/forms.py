from django import forms
from .models import Evento

class EventoForm(form.ModelForm):
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