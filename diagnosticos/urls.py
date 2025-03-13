from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('diagnosticos/', views.diagnosticoList),
    path('diagnosticoCreate/', views.diagnosticoCreate, name = 'diagnosticoCreate')]
