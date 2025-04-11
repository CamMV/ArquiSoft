from django.db.models.signals import post_save
from django.dispatch import receiver
from eventos.models import Evento
from resultados.models import Resultado
import random

@receiver(post_save, sender=Evento)
def crear_resultado_automaticamente(sender, instance, created, **kwargs):
    if created:
        valor = random.randint(1, 100)  # Genera un valor aleatorio entre 1 y 100
        if valor< 50:
            recomendaciones = "No se requiere tratamiento adicional."
        else:
            recomendaciones = "Se recomienda realizar un seguimiento."
        Resultado.objects.create(
            evento=instance,
            valor=valor,
            recomendaciones=recomendaciones
        )