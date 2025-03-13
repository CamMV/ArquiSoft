from django.contrib import admin
from django.urls import path
from . import views

urlptterns = [
    path('', views.imagenesView, name = 'imagenes view'),
    path('<int:pk>/', views.imagenView, name = 'imagen view'),
]