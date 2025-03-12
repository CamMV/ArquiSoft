from django.urls import path
from .views import obtener_reporte

urlpatterns = [
    path('<int:resultado_id>/reporte/', obtener_reporte, name='obtener_reporte'),
]
