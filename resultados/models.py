from django.db import models


from django.utils.timezone import now


from pacientes.models import Paciente
from diagnosticos.models import Diagnostico
from eventos.models import Evento

from django.db.models import Prefetch

class Resultado(models.Model):

    
    contenido = models.TextField()
    recomendaciones = models.TextField(blank=True, null=True)
    fecha_generacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Resultado: {self.contenido}, Recomendaciones: {self.recomendaciones}  ,Fecha de generacion: {self.fecha_generacion}"



#Guardado en base de datos
"""  def save(self, *args, **kwargs):


        super().save(*args, **kwargs)  

        Evento.objects.create(

            paciente=self.paciente,
            tipo='INFORME_FINAL',
            descripcion=f"Se generó un informe final para {self.paciente.nombre}."
        )
   """
   