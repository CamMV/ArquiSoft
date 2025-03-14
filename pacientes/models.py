from django.db import models

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    historia_clinica = models.CharField(max_length=250) #De momento no esta conectado con ninguna app o cmoponente de django, esto se cambia despues


    def __str__(self):
        return f"{self.nombre} ({self.edad} años)"
