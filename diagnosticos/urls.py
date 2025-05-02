from django.urls import path
from . import views

urlpatterns = [
    path('', views.diagnosticoList, name='diagnosticoList'),
    path('diagnosticocreate/', views.diagnostico_create, name='diagnosticoCreate'),
    path('<int:diagnostico_id>/', views.diagnosticoInfo, name='diagnosticoInfo'),
    path('email/', views.diagnosticoEmail, name='diagnosticoEmail'),
]