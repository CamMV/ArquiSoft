from django.db import models



class Paciente(models.Model):

    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()

    historia_clinica = models.TextField()


    def __str__(self):
        return f"{self.nombre} ({self.edad} años)"
