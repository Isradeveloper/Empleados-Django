from django.shortcuts import render
#Importar vistas genericas
from django.views.generic import ListView, DetailView, CreateView, TemplateView
#Importamos modelos
from .models import Empleados

from django.urls import reverse_lazy

# Create your views here.

# Listar todos los empleados de la empresa
# En url agregar ?page=1,2..n
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

# Listar habilidades de un empleado N:M
class ListHabilidadesEmpleado(ListView):
  template_name = 'empleados/habilidades.html'
  context_object_name = 'habilidades'

  def get_queryset(self):
    numero_id = self.request.GET.get('id',)
    if (numero_id == ''):
      return []
    empleado = Empleados.objects.get(id=numero_id)
    habilidades = empleado.habilidades.all()
    return habilidades

# Acceder a la información de los empleados
class EmpleadosDetailView(DetailView):
    model = Empleados
    template_name = "empleados/detail_empleados.html"

    # Agregar variables a la view
    def get_context_data(self, **kwargs):
        context = super(EmpleadosDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context


class EmpleadosCreateView(CreateView):
    model = Empleados
    template_name = "empleados/crear_empleado.html"
    # fields = ['nombres', 'apellidos', 'profesion']
    fields = ('__all__')
    # Se recargue misma pagina
    # success_url = '.' 

    # success_url = '/success'

    success_url = reverse_lazy('empleados_app:correcto')


class successView(TemplateView):
    template_name = "empleados/success.html"
