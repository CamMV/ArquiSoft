from imagenes.models import Imagenes

def getImagenes():
    imagenes = Imagenes.objects.all()
    return imagenes

def getImagen(imagen_pk):
    imagen = Imagenes.objects.get(pk=imagen_pk)
    return imagen

def updateImagen(imagen_pk, new_imagen):
    imagen = getImagen(imagen_pk)
    imagen["nombre"] = new_imagen["nombre"]
    imagen["descripcion"] = new_imagen["descripcion"]
    imagen["imagen"] = new_imagen["imagen"]
    imagen.save()
    return imagen

def createImagen(name, description, image):
    imagen = Imagenes.objects.create(nombre=name, descripcion=description, imagen=image)
    return imagen