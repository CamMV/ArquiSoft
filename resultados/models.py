from django.db import models

class Resultado(models.Model):
    valor = models.IntegerField(default=True, null=False)  
    recomendaciones = models.TextField(blank=True, null=True)
    fecha_generacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Recomendaciones: {self.recomendaciones}, Fecha de generación: {self.fecha_generacion}, Valor del resultado: {self.valor}"
