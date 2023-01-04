from django.shortcuts import render
#Importar vistas genericas
from django.views.generic import ListView
#Importamos modelos
from .models import Empleados

# Create your views here.

# Listar todos los empleados de la empresa
class ListAllEmpleados(ListView):
  template_name = 'empleados/list_all.html'
  paginate_by = 2
  ordering = ['nombres']
  model = Empleados

# Listar los empleados que pertenecen a un area de la empresa
class ListEmpleadosArea(ListView):
  template_name = 'empleados/list_by_area.html'
  model = Empleados

  def get_queryset(self):
    area = self.kwargs['nombre_corto']
    lista = Empleados.objects.filter (
      departamento__nombre_corto = area
    )
    return lista

# Listar empleados por trabajo
class ListEmpleadosTrabajo(ListView):
  template_name = 'empleados/list_by_job.html'
  model = Empleados

  def get_queryset(self):
    job = self.kwargs['profesion']
    lista = Empleados.objects.filter(
      profesion = job
    )
    return lista

# Listar los empleados por palabra clave
class ListEmpleadosPalabraClave(ListView):
  """Listar empleados por palabra clave"""

  template_name = 'empleados/list_by_kword.html'
  model = Empleados
  context_object_name = 'empleados'

  def get_queryset(self):
    buscar = self.request.GET.get('kword',)

    lista = Empleados.objects.filter(
      nombres__icontains=buscar
    )

    return lista
# Listar habilidades de un empleado
