from django.db import models
from imagenes.models import Imagenes, EEG, MRI, mRNA
from resultados.models import Resultado


class Diagnostico(models.Model):
    #Aquí se encuentran las inyecciones de dependiencias en la clase diagnostico
    imagen = models.ForeignKey(Imagenes, on_delete=models.CASCADE, blank=True, default=None)
    eeg = models.ForeignKey(EEG, on_delete=models.CASCADE, blank=True, default=None)
    mri = models.ForeignKey(MRI, on_delete=models.CASCADE,  blank=True, default=None)
    mrna = models.ForeignKey(mRNA, on_delete=models.CASCADE,  blank=True, default=None)
    resultado = models.ForeignKey(Resultado, on_delete=models.CASCADE, blank=True, default=None)
    fecha = models.DateTimeField(auto_now_add=True)
    contenido = models.CharField(default="Sin contenido", max_length=250, null = True, blank = True)    
    

#inyectamos imagenes y resultados