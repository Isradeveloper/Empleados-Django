from django.urls import path
from . import views

urlpatterns = [
    path('listar_empleados/', views.ListAllEmpleados.as_view()),
    path('listar_empleados_area/<nombre_corto>/', views.ListEmpleadosArea.as_view()),
]