# resultados/models.py
from django.db import models
from eventos.models import Evento

class Resultado(models.Model):
    evento = models.OneToOneField(Evento, on_delete=models.CASCADE, related_name='resultado')
    valor = models.IntegerField(default=0)
    recomendaciones = models.CharField(max_length=250)
    fecha_generacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Recomendaciones: {self.recomendaciones}, Fecha: {self.fecha_generacion}, Valor: {self.valor}"