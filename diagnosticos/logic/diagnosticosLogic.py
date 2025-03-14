from diagnosticos.models import Diagnostico
from django.db import models
from django.utils import timezone


def getDiagnosticos():
    diagnosticos = Diagnostico.objects.all()
    return diagnosticos

def getDiagnostico(diagnostico_pk):
    diagnostico = Diagnostico.objects.get(diagnostico_pk)
    return diagnostico

def updateDiagnostico(diagnostico_pk, new_diagnostico):
    diagnostico = getDiagnostico(diagnostico_pk)
    diagnostico["imagen"] = new_diagnostico["imagen"]
    diagnostico["eeg"] = new_diagnostico["eeg"]
    diagnostico["mri"] = new_diagnostico["mri"]
    diagnostico["mrina"] = new_diagnostico["mrina"]
    diagnostico["resultado"] = new_diagnostico["resultado"]
    diagnostico["fecha"] = new_diagnostico["fecha"]
    diagnostico["contenido"] = new_diagnostico["contenido"]
    return diagnostico

def createDiagnostico(imagen, eeg, mri, mrina, resultado):
    fecha_creacion = models.DateTimeField(default=timezone.now)
    if Diagnostico.resultado < 50:
        contenido = fecha_creacion + " " + "Es poco probable que el paciente tenga Epilepsia"
    else:
        contenido = fecha_creacion + " " + "Es probable que el paciente tenga Epilepsia"
    diagnostico = Diagnostico.objects.create(imagen=imagen, eeg=eeg, mri=mri, mrina=mrina, resultado=resultado, fecha=fecha_creacion, contenido=contenido)
    return diagnostico
    