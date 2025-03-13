from django.contrib import admin
from django.urls import path
from . import views

urlptterns = [
    path('', views.pacientesView, name = 'pacientes view'),
    path('<int:pk>/', views.pacienteView, name = 'paciente view'),
]