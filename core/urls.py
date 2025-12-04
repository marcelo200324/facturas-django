from django.urls import path
from . import views

urlpatterns = [
    path('', views.crear_factura, name='crear_factura'),
    path('resumen-semanal/', views.resumen_semanal, name='resumen_semanal'),
    path('historial/', views.historial_semanas, name='historial'),
    path('exportar-word/', views.exportar_semana_word, name='exportar_word'),
    path('editar/<int:factura_id>/', views.editar_factura, name='editar_factura'),
    path('eliminar/<int:factura_id>/', views.eliminar_factura, name='eliminar_factura'),
]

