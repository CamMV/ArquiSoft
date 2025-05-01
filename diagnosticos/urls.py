from django.urls import path
from . import views

urlpatterns = [
    path('', views.diagnosticoList, name='diagnosticoList'),
    path('crear/', views.diagnostico_create, name='diagnosticoCreate'),
]