from django.db import models



from eventos.models import Evento

from django.apps import apps



class Diagnostico(models.Model):



    paciente = models.ForeignKey("pacientes.Paciente", on_delete=models.CASCADE)


    eeg = models.ForeignKey("imagenes.EEG", on_delete=models.SET_NULL, null=True, blank=True)
    mri = models.ForeignKey("imagenes.MRI", on_delete=models.SET_NULL, null=True, blank=True)
    mirna = models.ForeignKey("imagenes.miRNA", on_delete=models.SET_NULL, null=True, blank=True)


    resultado = models.TextField()

    fecha = models.DateTimeField(auto_now_add=True)



    def save(self, *args, **kwargs):
       
        super().save(*args, **kwargs)  
        Evento.objects.create(
            paciente=self.paciente,
            tipo='DIAGNOSTICO_NUEVO',
            descripcion=f"Se generó un diagnóstico para {self.paciente.nombre}."
        )
