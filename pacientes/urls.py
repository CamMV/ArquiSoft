from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlptterns = [
    path('', views.pacienteList, name = 'pacienteList'),
    path('pacientecreate/', csrf_exempt(views.paciente_create), name = 'pacientecreate'),
]