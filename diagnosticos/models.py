from django.db import models
from resultados.models import Resultado

class Diagnostico(models.Model):
    resultado = models.ForeignKey(Resultado, on_delete=models.CASCADE, related_name='diagnosticos')
    diagnostico = models.CharField(max_length=1000)
    fecha_diagnostico = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Diagnóstico: {self.diagnostico}, Fecha: {self.fecha_diagnostico}"
    
    
class IntentoModificacionDiagnostico(models.Model):
    user = models.CharField(max_length=255)  
    diagnostico = models.ForeignKey(Diagnostico, on_delete=models.CASCADE)
    intentos = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user} - {self.diagnostico} - {self.intentos} intentos"

