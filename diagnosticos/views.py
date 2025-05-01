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
            diagnostico = form.save()

            send_mail(
                subject='Nuevo diagnóstico creado',
                message=f'Se ha creado un nuevo diagnóstico: {diagnostico.diagnostico}. con una disponibilidad del 99.9%',
                from_email=None,  
                recipient_list=['santigs2005@gmail.com', 'johan5murciav@gmail.com'],  # Los que recibirán el correo
                fail_silently=False,
            )

            messages.success(request, 'Disponibilidad del diagnostico 99.9%')
            return redirect('diagnosticoList')
    else:
        form = DiagnosticoForm()
    
    context = {
        'form': form
    }
    return render(request, 'Diagnostico/diagnosticoCreate.html', context)
