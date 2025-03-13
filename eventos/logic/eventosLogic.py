from models import Evento

def getEventos():
    eventos = Evento.objects.all()
    return eventos

def getEvento(evento_pk):
    evento = Evento.objects.get(pk=evento_pk)
    return evento

