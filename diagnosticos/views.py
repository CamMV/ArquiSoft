from .logic import diagnosticosLogic as il
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

def diagnosticosView(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            diagnostico_dto = il.getDiagnostico(id)
            diagnostico = serializers.serialize('json', [diagnostico_dto,])
            return HttpResponse(diagnostico, 'application/json')
        else:
            diagnosticos_dto = il.getDiagnosticos()
            diagnosticos = serializers.serialize('json', diagnosticos_dto)
            return HttpResponse(diagnosticos, 'application/json')
    
    if request.method == 'POST':
        diagnostico_dto = il.createDiagnostico(id, json.loads(request.body),None)
        diagnostico = serializers.serialize('json', [diagnostico_dto,])
        return HttpResponse(diagnostico, 'application/json')

@csrf_exempt
def diagnosticoView(request, pk):
    if request.method == 'GET':
        diagnostico_dto = il.getDiagnostico(pk)
        diagnostico = serializers.serialize('json', [diagnostico_dto,])
        return HttpResponse(diagnostico, 'application/json')
    
    if request.method == 'PUT':
        diagnostico_dto = il.updateDiagnostico(pk, json.loads(request.body))
        diagnostico = serializers.serialize('json', [diagnostico_dto,])
        return HttpResponse(diagnostico, 'application/json')