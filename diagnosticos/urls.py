from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.diagnosticosView, name = 'diagnosticos view'),
    path('<int:pk>/', views.diagnosticoView, name = 'diagnostico view'),
    ]


