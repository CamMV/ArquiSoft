from models import Resultado

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

def createResultado(name, date, patient):
    resultado = Resultado.objects.create(nombre=name, fecha=date, paciente=patient)
    return resultado
