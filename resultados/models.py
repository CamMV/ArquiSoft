# resultados/models.py
from django.db import models
from dignosticos.models import Diagnostico

class Resultado(models.Model):
    diagnostico = models.OneToOneField(Diagnostico, on_delete=models.CASCADE, related_name='resultado')
    valor = models.IntegerField(default=0)
    recomendaciones = models.CharField(max_length=250)
    fecha_generacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Recomendaciones: {self.recomendaciones}, Fecha: {self.fecha_generacion}, Valor: {self.valor}"