from django.urls import path
from . import views

app_name = 'empleados_app'

urlpatterns = [
    path('listar_empleados/', views.ListAllEmpleados.as_view()),
    path('listar_empleados_area/<nombre_corto>/', views.ListEmpleadosArea.as_view()),
    path('listar_empleados_profesion/<profesion>/', views.ListEmpleadosTrabajo.as_view()),
    path('listar_empleados_busqueda', views.ListEmpleadosPalabraClave.as_view()),
    path('listar_habilidades_empleado', views.ListHabilidadesEmpleado.as_view()),
    path('ver_empleados/<pk>/', views.EmpleadosDetailView.as_view()),
    path('agregar_empleado/', views.EmpleadosCreateView.as_view()),
    path('success/', views.successView.as_view(), name='correcto'),
]