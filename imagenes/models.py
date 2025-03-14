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


class mRNA(models.Model):
    
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    
class Imagenes(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=250)
    imagen = models.ImageField(upload_to='images/')
 
    def __str__(self):
        return f"{self.nombre}, {self.descripcion}"
