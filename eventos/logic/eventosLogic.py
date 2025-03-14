from ..models import Evento


def getEventos():
    eventos = Evento.objects.all().order_by('-dateTime')[:10]
    return eventos

def createEvento(form):
    if form is None:
        return ()
    else:
        form.save()
        return ()
