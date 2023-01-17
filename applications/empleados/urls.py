from django.urls import path
from . import views

app_name = 'empleados_app'

urlpatterns = [
    path('listar_empleados/', views.ListAllEmpleados.as_view(), name='all'),
    path('listar_empleados_datatable/', views.ListAllEmpleadosDataTable.as_view(), name='all_data_table'),
    path('listar_empleados_area/<nombre_corto>/', views.ListEmpleadosArea.as_view()),
    path('listar_empleados_profesion/<profesion>/', views.ListEmpleadosTrabajo.as_view()),
    path('listar_empleados_busqueda', views.ListEmpleadosPalabraClave.as_view()),
    path('listar_habilidades_empleado', views.ListHabilidadesEmpleado.as_view()),
    path('ver_empleados/<pk>/', views.EmpleadosDetailView.as_view(), name='ver'),
    path('agregar_empleado/', views.EmpleadosCreateView.as_view()),
    path('success/', views.successView.as_view(), name='correcto'),
    path('actualizar_empleado/<pk>/', views.EmpleadoUpdateView.as_view(), name='actualizar'),
    path('eliminar_empleado/<pk>/', views.EmpleadoDeleteView.as_view(), name='eliminar')
] 