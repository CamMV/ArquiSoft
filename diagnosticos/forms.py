# diagnosticos/forms.py
from django import forms
from .models import Diagnostico
from resultados.models import Resultado

class DiagnosticoForm(forms.ModelForm):
    resultado = forms.ModelChoiceField(
        queryset=Resultado.objects.all(), 
        label="Resultado asociado"
    )

    class Meta:
        model = Diagnostico
        fields = ['resultado', 'diagnostico']
