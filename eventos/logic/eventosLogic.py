from ..models import Evento


def getEventos():
    eventos = Evento.objects.all().order_by('-dateTime')[:10]
    return eventos

def createEvento(form):
    evento = form.save()
    evento.save()
    return ()
    
