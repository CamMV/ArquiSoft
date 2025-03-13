from django.shortcuts import render
from .forms import EventoForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.eventosLogic import createEvento, getEventos

# Create your views here.
def eventoList(request):
    eventos = getEventos()
    context = {
        'evento_list' : eventos
    }
    return render(request, 'Evento/eventos.html', context)

def evento_create(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_vaid():
            createEvento(form)
            messages.add_message(request, messages.SUCCESS, 'Evento creado con exito')
            return HttpResponseRedirect(reverse('EventoCreado'))
        else:
            print(form.errors)
    else:
        form = EventoForm()
        
    context = {
        'fomr': form
    }
    return render(request, 'Evento/eventoCreate.html', context)
            