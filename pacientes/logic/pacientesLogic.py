from ..models import Paciente

def getPacientes():
    pacientes = Paciente.objects.all()
    return pacientes

def getPaciente(pac_pk):
    paciente = Paciente.objects.get(pk=pac_pk)
    return paciente

def updatePaciente(pac_pk, new_pac):
    paciente = getPaciente(pac_pk)
    paciente.nombre = new_pac["nombre"]
    paciente.edad = new_pac["edad"]
    paciente.historia_clinica = new_pac["historia_clinica"]
    paciente.save()
    return paciente

def createPaciente(form):
    paciente = form.save()
    paciente.save()
    return ()

