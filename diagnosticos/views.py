from django.shortcuts import render, redirect
from .forms import DiagnosticoForm
from django.contrib import messages
from .logic.diagnosticosLogic import getDiagnosticos

# Vista para listar todos los diagnósticos
def diagnosticoList(request):
    diagnosticos = getDiagnosticos()
    context = {
        'diagnosticos_list': diagnosticos
    }
    return render(request, 'Diagnostico/diagnosticos.html', context)

# Vista para crear un diagnóstico
def diagnostico_create(request):
    if request.method == 'POST':
        form = DiagnosticoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Diagnóstico creado con éxito')
            return redirect('diagnosticoCreate')  # Redirige para crear otro o podrías ir al listado
    else:
        form = DiagnosticoForm()
    
    context = {
        'form': form
    }
    return render(request, 'Diagnostico/diagnosticoCreate.html', context)

