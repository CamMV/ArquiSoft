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
            self.descripcion = "Orden médica en la que un profesional de la salud indica el uso de un medicamento específico, detallando la dosis, la frecuencia y la duración del tratamiento según las necesidades del paciente."
        elif self.tipo == 'CONSULTA_MEDICA':
            self.descripcion =  "Encuentro entre un paciente y un profesional de la salud donde se evalúan síntomas, se diagnostican enfermedades y se establecen tratamientos o recomendaciones para el bienestar del paciente."
        elif self.tipo == 'EXAMEN_MEDICO':
            self.descripcion =  " Evaluación realizada por un profesional de la salud para diagnosticar o monitorear una condición médica. Puede incluir pruebas físicas, análisis de laboratorio o estudios de imagen."
        elif self.tipo == 'CIRUGIAL':
            self.tipo = "Procedimiento médico en el que se realiza una intervención en el cuerpo del paciente, ya sea con fines terapéuticos, diagnósticos o estéticos, y que puede requerir anestesia y hospitalización."
        elif self.tipo == 'CITA_MEDICA':
            self.descripcion = "Programación de una visita a un centro de salud para recibir atención médica, ya sea para una consulta, seguimiento de tratamiento, realización de exámenes o cualquier otro servicio de salud."
            
        super().save(*args, **kwargs)
        
        