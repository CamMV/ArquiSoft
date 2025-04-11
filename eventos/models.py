from django.db import models
from django.utils import timezone
from pacientes.models import Paciente

class Evento(models.Model):

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, blank=True, default=None)
    tipo = models.CharField(max_length=50, choices=[
        ('MUESTRA_DE_SANGRE', 'Muestra de sangre'),
        ('PRESCRIPCION_dE_MEDICAMENTO', 'Prescripcion de medicamento'),
        ('CONSULTA_MEDICA', 'Consulta medica'),
        ('EXAMEN_MEDICO', 'Examen medico'),
        ('CIRUGIAL', 'Cirugia'),
        ('CITA_MEDICA', 'Cita medica'),
    ])
    descripcion = models.CharField(max_length=50)
    fecha = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return f"Paciente: {self.paciente}, Evento: {self.tipo}, Descripción: {self.descripcion}, Fecha: {self.fecha}"
