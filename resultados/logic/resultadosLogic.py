from models import Resultado
import random
from django.db import models as md
from django.utils import timezone

def getResultados():
    resultados = Resultado.objects.all()
    return resultados

def getResultado(res_pk):
    resultado = Resultado.objects.get(pk=res_pk)
    return resultado

def updateResultado(res_pk, new_res):
    resultado = getResultado(res_pk)
    resultado["contenido"] = new_res["contenido"]
    resultado["fecha_generacion"] = new_res["fecha_generacion"]
    resultado["recomendaciones"] = new_res["recomendaciones"]
    resultado.save()
    return resultado

def createResultado():
    valor = random.randint(1, 100)
    if valor < 50:
        recomendaciones = "Recomendacion para valor menor a 50"
    else:
        recomendaciones = "Recomendacion para valor mayor a 50"
    fecha_generacion = md.DateTimeField(default=timezone.now)
    resultado = Resultado.objects.create(valor=valor, recomendaciones=recomendaciones, fecha_generacion=fecha_generacion)
    return resultado
