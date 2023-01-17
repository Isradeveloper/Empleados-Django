from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from .forms import NewDepartamentoForm
from django.urls import reverse_lazy
from applications.empleados.models import Empleados
from .models import Departamentos
from django import forms

# Create your views here.

class NewDepartamentoView(FormView):
  template_name = 'departamentos/add.html'
  form_class = NewDepartamentoForm
  success_url = reverse_lazy('departamentos:success-add')

  def form_valid(self, form) :
  # Crea instancia
    depa = Departamentos(
      nombre = form.cleaned_data['nombre_departamento'],
      nombre_corto = form.cleaned_data['nombre_corto_departamento']
    )

    depa.save()

    # nombres = self.request.POST['nombres_empleado']
    nombres = form.cleaned_data['nombres_empleado']
    apellidos = form.cleaned_data['apellidos_empleado']

    Empleados.objects.create(
      nombres = nombres,
      apellidos = apellidos,
      profesion = 0,
      departamento = depa
    )
  
    return super().form_valid(form)

  def clean_nombres_empleado(self):
    nombres_empleado = self.cleaned_data.get('nombres_empleado')

    # TODO Validation

    if len(nombres_empleado) <= 2:
      raise forms.ValidationError('El nombre del empleado debe tener más de 2 carácteres')
  
    return nombres_empleado

class SuccessAdd(TemplateView):
  print('*********************************')
  template_name = "departamentos/success.html"


