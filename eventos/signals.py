from django.db.models.signals import post_save
from django.dispatch import receiver
from eventos.models import Evento
from resultados.models import Resultado

@receiver(post_save, sender=Evento)
def crear_resultado_automaticamente(sender, instance, created, **kwargs):
    if created:
        Resultado.objects.create(
            evento=instance,
            valor=0,
            recomendaciones="Pendiente de evaluación"
        )