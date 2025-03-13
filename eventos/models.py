from django.db import models
from django.utils import timezone
from pacientes.models import Paciente
from diagnosticos.models import Diagnostico

class Evento(models.Model):

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True, blank=True)
    diagnostico = models.ForeignKey(Diagnostico, on_delete=models.CASCADE, null=True, blank=True)
    tipo = models.CharField(max_length=50, choices=[
        ('MUESTRA_DE_SANGRE', 'Muestra de sangre'),
        ('PRESCRIPCION_dE_MEDICAMENTO', 'Prescripcion de medicamento'),
        ('CONSULTA_MEDICA', 'Consulta medica'),
        ('EXAMEN_MEDICO', 'Examen medico'),
        ('CIRUGIAL', 'Cirugia'),
        ('CITA_MEDICA', 'Cita medica'),
    ])
    descripcion = models.TextField()
    fecha = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return f"Paciente: {paciente}, Evento: {self.tipo}, Descripción: {self.descripcion}, Fecha: {self.fecha}, Diagnóstico: {self.diagnostico}"

    def save(self, *args, **kwargs):
        if self.tipo == 'MUESTRA_DE_SANGRE':
            self.descripcion = "Procedimiento en el que se extrae una pequeña cantidad de sangre del paciente para su análisis en un laboratorio, con el objetivo de diagnosticar enfermedades, evaluar el estado de salud o monitorear un tratamiento."
        elif self.tipo == 'PRESCRIPCION_dE_MEDICAMENTO':
            pass