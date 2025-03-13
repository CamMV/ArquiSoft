from .logic import pacientesLogic as pl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

def pacientesView(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            paciente_dto = pl.getPaciente(id)
            paciente = serializers.serialize('json', [paciente_dto,])
            return HttpResponse(paciente, 'application/json')
        else:
            pacientes_dto = pl.getPacientes()
            pacientes = serializers.serialize('json', pacientes_dto)
            return HttpResponse(pacientes, 'application/json')
    
    if request.method == 'POST':
        paciente_dto = pl.createPaciente(json.loads(request.body))
        paciente = serializers.serialize('json', [paciente_dto,])
        return HttpResponse(paciente, 'application/json')
    
    

@csrf_exempt
def pacienteView(request, pk):
    if request.method == 'GET':
        paciente_dto = pl.getPaciente(pk)
        paciente = serializers.serialize('json', [paciente_dto,])
        return HttpResponse(paciente, 'application/json')
    
    if request.method == 'PUT':
        paciente_dto = pl.updatePaciente(pk, json.loads(request.body))
        paciente = serializers.serialize('json', [paciente_dto,])
        return HttpResponse(paciente, 'application/json')