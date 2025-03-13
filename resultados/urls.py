from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.resultadosView, name = 'resultados view'),
    path('<int:pk>/', views.resultadoView, name = 'resultado view'),
]
