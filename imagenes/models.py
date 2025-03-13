from django.db import models

from pacientes.models import Paciente

class EEG(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    archivo = models.FileField(upload_to="eeg/")
    fecha = models.DateTimeField(auto_now_add=True)

class MRI(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="mri/")
    fecha = models.DateTimeField(auto_now_add=True)


class miRNA(models.Model):
    
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    resultados = models.JSONField()
    fecha = models.DateTimeField(auto_now_add=True)
    
class Imagenes(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='images/')
    objects = models.Manager()  
    def __str__(self):
        return f"{self.nombre}, {self.descripcion}"
