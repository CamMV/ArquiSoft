from django.db import models

from pacientes.models import Paciente


from imagenes.models import EEG, MRI, miRNA

class Evento(models.Model):

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True, blank=True)
    diagnostico = models.ForeignKey("diagnosticos.Diagnostico", on_delete=models.SET_NULL, null=True, blank=True)
    tipo = models.CharField(max_length=50, choices=[
        ('ALERTA_MEDICA', 'Alerta Médica'),
        ('DIAGNOSTICO_NUEVO', 'Nuevo Diagnóstico'),
        ('ACTUALIZACION_PACIENTE', 'Actualización de Datos del Paciente'),
        ('NUEVO_ESTUDIO', 'Nuevo Estudio Médico'),
        ('INFORME_FINAL', 'Reporte Generado')
    ])
    descripcion = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Paciente: {paciente}, Evento: {self.tipo}, Descripción: {self.descripcion}, Fecha: {self.fecha}, Diagnóstico: {self.diagnostico}"
