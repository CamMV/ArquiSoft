from ..models import Diagnostico
from resultados.models import Resultado
from django.utils import timezone

def getDiagnosticos():
    return Diagnostico.objects.all()

def getDiagnostico(diagnostico_pk):
    return Diagnostico.objects.get(pk=diagnostico_pk)

def createDiagnostico(data):
    resultado = Resultado.objects.get(pk=data["resultado_id"])
    diagnostico_texto = data["diagnostico"]
    
    nuevo_diagnostico = Diagnostico.objects.create(
        resultado=resultado,
        diagnostico=diagnostico_texto,
        fecha_diagnostico=timezone.now()
    )
    return nuevo_diagnostico

def updateDiagnostico(diagnostico_pk, new_data):
    diagnostico = getDiagnostico(diagnostico_pk)
    diagnostico.diagnostico = new_data["diagnostico"]
    diagnostico.save()
    return diagnostico
