from .logic import resultadosLogic as rl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def resultadosView(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            resultado_dto = rl.getResultado(id)
            resultado = serializers.serialize('json', [resultado_dto,])
            return HttpResponse(resultado, 'application/json')
        else:
            resultados_dto = rl.getResultados()
            resultados = serializers.serialize('json', resultados_dto)
            return HttpResponse(resultados, 'application/json')
    
    if request.method == 'POST':
        resultado_dto = rl.createResultado(json.loads(request.body))
        resultado = serializers.serialize('json', [resultado_dto,])
        return HttpResponse(resultado, 'application/json')

@csrf_exempt
def resultadoView(request, pk):
    if request.method == 'GET':
        resultado_dto = rl.getResultado(pk)
        resultado = serializers.serialize('json', [resultado_dto,])
        return HttpResponse(resultado, 'application/json')
    
    if request.method == 'PUT':
        resultado_dto = rl.updateResultado(pk, json.loads(request.body))
        resultado = serializers.serialize('json', [resultado_dto,])
        return HttpResponse(resultado, 'application/json')