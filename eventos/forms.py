from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):
    paciente = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    diagnostico = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
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
            'tipo': "Tipo",
            'diagnostico': "Diagnostico",
            'descripcion': "Descripcion"
            #'fecha' : "Fecha",
        }