from .logic import imagenesLogic as il
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt

def imagenesView(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            imagen_dto = il.getImagen(id)
            imagen = serializers.serialize('json', [imagen_dto,])
            return HttpResponse(imagen, 'application/json')
        else:
            imagenes_dto = il.getImagenes()
            imagenes = serializers.serialize('json', imagenes_dto)
            return HttpResponse(imagenes, 'application/json')
    
    if request.method == 'POST':
        imagen_dto = il.createImagen(id, json.loads(request.body),None)
        imagen = serializers.serialize('json', [imagen_dto,])
        return HttpResponse(imagen, 'application/json')
    
@csrf_exempt
def imagenView(request, pk):
    if request.method == 'GET':
        imagen_dto = il.getImagen(pk)
        imagen = serializers.serialize('json', [imagen_dto,])
        return HttpResponse(imagen, 'application/json')
    
    if request.method == 'PUT':
        imagen_dto = il.updateImagen(pk, json.loads(request.body))
        imagen = serializers.serialize('json', [imagen_dto,])
        return HttpResponse(imagen, 'application/json')