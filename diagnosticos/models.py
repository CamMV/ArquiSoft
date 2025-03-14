from django.db import models
from imagenes.models import Imagenes, EEG, MRI, mRNA
from resultados.models import Resultado

class Diagnostico(models.Model):
    imagen = models.ForeignKey(Imagenes, on_delete=models.CASCADE, blank=True, null=True, default=None)
    eeg = models.CharField(default="Sin resultados", max_length=250, null=True, blank=True)
    mri = models.CharField(default="Sin resultados", max_length=250, null=True, blank=True)
    mrna = models.CharField(default="Sin resultados", max_length=250, null=True, blank=True)
    resultado = models.ForeignKey(Resultado, on_delete=models.CASCADE, blank=True, null=True, default=None)
    fecha = models.DateTimeField(auto_now_add=True)
    contenido = models.CharField(default="Sin contenido", max_length=250, null=True, blank=True)   
    
#inyectamos imagenes y resultados