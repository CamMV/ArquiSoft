from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('diagnosticos/', views.diagnosticoList),
    path('diagnosticoCreate/', csrf_exempt(views.diagnostico_create), name = 'diagnosticoCreate')
    ]
