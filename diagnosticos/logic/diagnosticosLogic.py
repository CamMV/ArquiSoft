
from ..models import Diagnostico
from resultados.models import Resultado

def getDiagnosticos():
    return Diagnostico.objects.all()

def getDiagnostico(diagnostico_pk):
    return Diagnostico.objects.get(pk=diagnostico_pk)

def updateDiagnostico(diagnostico_pk, new_data):
    diagnostico = getDiagnostico(diagnostico_pk)
    diagnostico.diagnostico = new_data["diagnostico"]
    diagnostico.save()
    return diagnostico
