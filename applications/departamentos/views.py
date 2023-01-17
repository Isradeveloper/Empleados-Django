from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView, ListView, DetailView
from .forms import NewDepartamentoForm
from django.urls import reverse_lazy
from applications.empleados.models import Empleados
from .models import Departamentos
from django import forms

# Create your views here.


class DepartamentosListView(ListView):
    model = Departamentos
    template_name = "departamentos/all.html"
    context_object_name = 'lista'


class DepartamentosDetailView(DetailView):
    model = Departamentos
    template_name = "departamentos/ver.html"

    
    def get_context_data(self, **kwargs):
        context = super(DepartamentosDetailView, self).get_context_data(**kwargs)
        return context
    


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


class SuccessAdd(TemplateView):
  print('*********************************')
  template_name = "departamentos/success.html"


