from django.db import models


from django.utils.timezone import now


from pacientes.models import Paciente
from diagnosticos.models import Diagnostico
from eventos.models import Evento

from django.db.models import Prefetch

class Resultado(models.Model):

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    diagnostico = models.ForeignKey("diagnosticos.Diagnostico", on_delete=models.CASCADE, related_name="resultados")
    eventos_relacionados = models.ManyToManyField("eventos.Evento", blank=True, related_name="resultados_relacionados")


    contenido = models.TextField()

    recomendaciones = models.TextField(blank=True, null=True)

    fecha_generacion = models.DateTimeField(auto_now_add=True)

    def generar_reporte(self):
        
        diagnostico = Diagnostico.objects.select_related("paciente").prefetch_related(
            Prefetch("eeg"),
            Prefetch("mri"),
            Prefetch("mirna")
        ).get(id=self.diagnostico.id)

        eventos = self.eventos_relacionados.values_list("tipo", flat=True) 




        reporte = f"""
        **Reporte Consolidado** 
        Paciente: {self.paciente.nombre} ({self.paciente.edad} años)
        Fecha: {now().strftime('%Y-%m-%d %H:%M')}
        --------------------------------------
        Diagnóstico:** {diagnostico.resultado}
        **Estudios Realizados:**
        - EEG: {'Presente' if diagnostico.eeg else 'No realizado'}
        - MRI: {'Presente' if diagnostico.mri else 'No realizado'}
        - miRNA: {'Presente' if diagnostico.mirna else 'No realizado'}
        
        **Eventos Relacionados:**
        {', '.join(eventos) if eventos else 'Ninguno'}

        **Recomendaciones:** {self.recomendaciones or 'No especificadas'}
        """



        return reporte





    def save(self, *args, **kwargs):


        super().save(*args, **kwargs)  

        Evento.objects.create(

            paciente=self.paciente,
            tipo='INFORME_FINAL',
            descripcion=f"Se generó un informe final para {self.paciente.nombre}."
        )
