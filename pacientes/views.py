from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import PacienteForm
from .logic.pacientesLogic import createPaciente, getPacientes


def pacienteList(request):
    paciente = getPacientes()
    context = {
        'paciente_list' : paciente
    }
    return render(request, 'Paciente/pacientes.html', context)


def paciente_create(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            createPaciente(form)
            messages.add_message(request, messages.SUCCESS, 'Paciente creado con exito')
            return HttpResponseRedirect(reverse('pacienteList'))
        else:
            print(form.errors)
    else:
        form = PacienteForm()
        
    context = {
        'form': form
    }
    return render(request, 'Paciente/pacienteCreate.html', context)