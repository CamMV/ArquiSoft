from django.shortcuts import render, redirect
from .forms import DiagnosticoForm
from django.contrib import messages
from .logic.diagnosticosLogic import getDiagnosticos, getDiagnostico, createDiagnostico
from django.http import JsonResponse
from django.core.mail import send_mail

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
            createDiagnostico(form)
            messages.success(request, 'Disponibilidad del diagnostico 99.9%')
            return redirect('diagnosticoList')
    else:
        form = DiagnosticoForm()
    
    context = {
        'form': form
    }
    return render(request, 'Diagnostico/diagnosticoCreate.html', context)

def diagnosticoInfo(request, diagnostico_id):
    if request.method == 'GET':
        diagnostico = getDiagnostico(diagnostico_id)
        if diagnostico is None:
            return JsonResponse({"error": "Diagnostico no encontrado"}, status=404)
        data = diagnostico.to_dict()
        return JsonResponse({"mensaje": "Diagnostico encontrado", "diagnostico": data}, status=200)
    return JsonResponse({"error": "Metodo no permitido"}, status=405)

def diagnosticoEmail(request):
    if request.method == 'GET':
        send_mail(
                subject='Nuevo diagnóstico buscado',
                message=f'Diagnostico buscado con una disponibilidad del 99.9%',
                from_email=None,  
                recipient_list=['santigs2005@gmail.com', 'johan5murciav@gmail.com'],  # Los que recibirán el correo
                fail_silently=False,
            )
        return redirect('diagnosticoList')
    return JsonResponse({"error": "Metodo no permitido"}, status=405)