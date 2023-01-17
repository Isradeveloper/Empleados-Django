from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy

from .models import Prueba
from .forms import PruebaForm

# Create your views here.

class IndexView(TemplateView):
  template_name = 'home/home.html'

class PruebaListView(ListView):
  template_name = 'home/lista.html'
  queryset = ['A', 'B', 'C']
  context_object_name = 'lista_prueba'


class ModeloListView(ListView):
    model = Prueba
    template_name = "home/lista_bd.html"
    context_object_name = "lista_prueba"


class PruebaCreateView(CreateView):
    model = Prueba
    template_name = "home/add.html"
    # No es necesario si utilizamos form class
    # fields = ('__all__')
    form_class = PruebaForm
    success_url = reverse_lazy('home_app:success')


class SuccessView(TemplateView):
    template_name = "home/success.html"

