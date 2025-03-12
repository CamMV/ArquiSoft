from django.db import models

from pacientes.models import Paciente
from django.apps import apps

class EEG(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    archivo = models.FileField(upload_to="eeg/")
    fecha = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
    
        super().save(*args, **kwargs)  
        Evento = apps.get_model('eventos', 'Evento')
        Evento.objects.create(
            paciente=self.paciente,
            tipo='NUEVO_ESTUDIO',
            descripcion=f"Nuevo EEG subido para {self.paciente.nombre}."
        )

class MRI(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="mri/")
    fecha = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
    
        super().save(*args, **kwargs) 
        Evento = apps.get_model('eventos', 'Evento')
        Evento.objects.create(
            paciente=self.paciente,
            tipo='NUEVO_ESTUDIO',
            descripcion=f"Nuevo MRI subido para {self.paciente.nombre}."
        )

class miRNA(models.Model):
    
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    resultados = models.JSONField()
    fecha = models.DateTimeField(auto_now_add=True)
