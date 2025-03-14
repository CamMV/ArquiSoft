from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import JsonResponse
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

def pacienteInfo(request):
    if request.method == "GET":
        return JsonResponse({"mensaje": "El paciente es altamente probable de padecer epilepsia"})
    return JsonResponse ({"error": "Metodo no permitido"}, status=405)