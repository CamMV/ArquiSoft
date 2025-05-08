from django.shortcuts import render, redirect
from .forms import DiagnosticoForm
from django.contrib import messages
from .logic.diagnosticosLogic import getDiagnosticos, getDiagnostico
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from proyecto.auth0backend import getRole
import hashlib
from django.views.decorators.csrf import csrf_exempt
from .models import Diagnostico, IntentoModificacionDiagnostico

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
            messages.add_message(request, messages.SUCCESS, 'Diagnóstico creado con éxito')
            return HttpResponseRedirect(reverse('diagnosticoCreate'))
        else:
            print(form.errors)
    else:
        form = DiagnosticoForm()

    context = {
        'form': form
    }
    return render(request, 'Diagnostico/diagnosticoCreate.html', context)

# Vista para obtener la información de un diagnóstico
def diagnosticoInfo(request, diagnostico_id):
    if request.method == 'GET':
        diagnostico = getDiagnostico(diagnostico_id)
        if diagnostico is None:
            return JsonResponse({"error": "Diagnóstico no encontrado"}, status=404)

        data = {
            "id": diagnostico.id,
            "resultado": diagnostico.resultado.id,
            "diagnostico": diagnostico.diagnostico,
            "fecha_diagnostico": diagnostico.fecha_diagnostico.strftime("%Y-%m-%d %H:%M:%S")
        }
        return JsonResponse({"mensaje": "Diagnóstico encontrado", "diagnostico": data}, status=200)

    return JsonResponse({"error": "Método no permitido"}, status=405)

# Vista para enviar email
def diagnosticoEmail(request):
    if request.method == 'GET':
        send_mail(
            subject='Nuevo diagnóstico buscado',
            message=f'Diagnóstico buscado con una disponibilidad del 99.9%',
            from_email=None,
            recipient_list=['santigs2005@gmail.com', 'johan5murciav@gmail.com'],
            fail_silently=False,
        )
        return redirect('diagnosticoList')
    return JsonResponse({"error": "Método no permitido"}, status=405)

# Vista para actualizar diagnóstico con validación de rol
@csrf_exempt
def diagnostico_update(request, diagnostico_id):
    diagnostico = getDiagnostico(diagnostico_id)

    if request.method == 'GET':
        # Renderizar el formulario con los datos actuales del diagnóstico
        context = {'diagnostico': diagnostico}
        return render(request, 'Diagnostico/diagnosticoUpdate.html', context)

    elif request.method == 'POST':
        user_role = getRole(request)

        if user_role != "Administrador":
            nuevo_diagnostico = request.POST.get("diagnostico")
            hash_actual = hashlib.sha256(diagnostico.diagnostico.encode()).hexdigest()
            hash_nuevo = hashlib.sha256(nuevo_diagnostico.encode()).hexdigest()

            if hash_actual != hash_nuevo:
                user_id = str(request.user)
                intento, created = IntentoModificacionDiagnostico.objects.get_or_create(
                    user=user_id,
                    diagnostico=diagnostico
                )
                intento.intentos += 1
                intento.save()

            return JsonResponse({"error": "No autorizado para modificar diagnósticos"}, status=403)

        nuevo_diagnostico = request.POST.get("diagnostico")
        diagnostico.diagnostico = nuevo_diagnostico
        diagnostico.save()
        return JsonResponse({"mensaje": "Diagnóstico modificado exitosamente"}, status=200)

    return JsonResponse({"error": "Método no permitido"}, status=405)


# Vista para ver intentos
def diagnostico_intentos(request):
    intentos = IntentoModificacionDiagnostico.objects.all()

    data = []
    for intento in intentos:
        data.append({
            "usuario": intento.user,
            "diagnostico_actual": intento.diagnostico.diagnostico,
            "intentos": intento.intentos
        })

    return JsonResponse({"intentos": data}, status=200)
