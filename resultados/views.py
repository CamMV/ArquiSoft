from django.shortcuts import render

from django.http import JsonResponse


from .models import Resultado



def obtener_reporte(request, resultado_id):


    try:

        resultado = Resultado.objects.get(id=resultado_id)
        reporte = resultado.generar_reporte()
        
        return JsonResponse({"reporte": reporte}, safe=False)
    

    except Resultado.DoesNotExist:
        return JsonResponse({"error": "Resultado no encontrado"}, status=404)
