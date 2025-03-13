from django.db import models
from imagenes.models import Imagenes, EEG, MRI, miRNA
from resultados.models import Resultado


class Diagnostico(models.Model):
    #Aquí se encuentran las inyecciones de dependiencias en la clase diagnostico
    imagen = models.ForeignKey(Imagenes, on_delete=models.SET_NULL, null=True, blank=True)
    eeg = models.ForeignKey(EEG, on_delete=models.SET_NULL, null=True, blank=True)
    mri = models.ForeignKey(MRI, on_delete=models.SET_NULL, null=True, blank=True)
    mirna = models.ForeignKey(miRNA, on_delete=models.SET_NULL, null=True, blank=True)
    resultado = models.ForeignKey(Resultado, on_delete=models.SET_NULL, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    conteindo = models.TextField()
    
    def valor_resultado(self):
        return self.resultado.valor > 50
#inyectamos imagenes y resultados