from django.shortcuts import render
from .forms import EventoForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from diagnosticos.models import Diagnostico
from .logic.eventosLogic import createEvento, getEventos

# Create your views here.
def eventoList(request):
    eventos = getEventos()
    context = {
        'evento_list' : eventos
    }
    return render(request, 'Evento/eventos.html', context)

def generarDiagnostico(paciente):
    contenido_predeterminado = f"Diagnóstico automático para {paciente}"
    diagnostico = Diagnostico.objects.create(contenido=contenido_predeterminado)
    if diagnostico is None:
        raise ("Diagnostico es none")
    else:
        return diagnostico

def evento_create(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.diagnostico = generarDiagnostico(evento.paciente)
            createEvento(evento)
            messages.add_message(request, messages.SUCCESS, 'Evento creado con exito')
            return HttpResponseRedirect(reverse('eventoCreate'))
        else:
            print(form.errors)
    else:
        form = EventoForm()
    context = {
        'form': form
    }
    return render(request, 'Evento/eventoCreate.html', context)