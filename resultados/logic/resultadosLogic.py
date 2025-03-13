from models import Resultado

def getResultados():
    resultados = Resultado.objects.all()
    return resultados

def getResultado(res_pk):
    resultado = Resultado.objects.get(pk=res_pk)
    return resultado

def updateResultado(res_pk, new_res):
    resultado = getResultado(res_pk)
    resultado["nombre"] = new_res["nombre"]
    resultado["fecha"] = new_res["fecha"]
    resultado["paciente"] = new_res["paciente"]
    resultado.save()
    return resultado

def createResultado(name, date, patient):
    resultado = Resultado.objects.create(nombre=name, fecha=date, paciente=patient)
    return resultado
