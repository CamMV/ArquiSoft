from django.db import models
import random
from resultados.models import Resultado

class Resultado(models.Model):
    valor = models.IntegerField(default==True, null=True)  
    recomendaciones = models.TextField(blank=True, null=True)
    fecha_generacion = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        
        if self.valor is None:  
            self.valor = random.randint(1, 100)
            
        if self.valor < 50:
            self.recomendaciones = "El valor del resultado es menor a 50"
        else:
            self.recomendaciones = "El valor del resultado es mayor o igual a 50"
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Recomendaciones: {self.recomendaciones}, Fecha de generación: {self.fecha_generacion}, Valor del resultado: {self.valor}"
