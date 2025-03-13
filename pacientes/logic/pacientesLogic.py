from models import Paciente

def getPacientes():
    pacientes = Paciete.objects.all()
    return pacientes

def getPaciente(pac_pk):
    paciente = Paciente.objects.get(pk=pac_pk)
    return paciente

def updatePciente(pac_pk, new_pac):
    paciente = getPaciente(pac_pk)
    paciente["nombre"] = new_pac["nombre"]
    paciente["edad"] = new_pac["edad"]
    paciente["historia_clinica"] = new_pac["historia_clinica"]
    paciente.save()
    return paciente

def createPaciente(name, age, hc):
    paciente = Paciente.objects.create(nombre=name, edad=age, historia_cljson=hc)
    return paciente

