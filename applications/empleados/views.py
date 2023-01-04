from django.shortcuts import render
#Importar vistas genericas
from django.views.generic import ListView
#Importamos modelos
from .models import Empleados

# Create your views here.

# Listar todos los empleados de la empresa
class ListAllEmpleados(ListView):
  template_name = 'empleados/list_all.html'
  model = Empleados

# Listar los empleados que pertenecen a un area de la empresa
# Listar empleados por trabajo
# Listar los empleados por palabra clave
# Listar habilidades de un empleado

