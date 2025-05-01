from django.urls import path
from . import views

urlpatterns = [
    path('', views.diagnosticoList, name='diagnosticoList'),
    path('diagnosticocreate/', views.diagnostico_create, name='diagnosticoCreate'),
]