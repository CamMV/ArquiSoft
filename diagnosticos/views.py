from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import DiagnosticoForm
from django.contrib import messages

def diagnostico_create(request):
    if request.method == 'POST':
        form = DiagnosticoForm(request.POST)
        if form.is_valid():
            diagnostico = form.save()

            send_mail(
                subject='Nuevo diagnóstico creado',
                message=f'Se ha creado un nuevo diagnóstico: {diagnostico.diagnostico}.',
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
    return render(request, 'diagnosticos/diagnosticoCreate.html', context)
