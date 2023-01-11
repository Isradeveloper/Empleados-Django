from django.db import models
from applications.departamentos.models import Departamentos
from ckeditor.fields import RichTextField


# Create your models here.

class Habilidades(models.Model):
  habilidad = models.CharField('Habilidad', max_length=50)

  class Meta:
    verbose_name = 'Habilidad'
    verbose_name_plural = 'Habilidades empleados'

  def __str__(self): 
    return (f'[{self.id}] {self.habilidad}')


class Empleados(models.Model):
  
  TRABAJO_CHOICES = (
    ('0', 'Ingeniero'),
    ('1', 'Economista'),
    ('2', 'Recursos humanos'),
    ('3', 'Obrero'),
  )

  nombres = models.CharField('Nombres', max_length=50)
  apellidos = models.CharField('Apellidos', max_length=50)
  full_name = models.CharField('Nombre completo', max_length=101, blank=True)
  profesion = models.CharField('Profesion', max_length=1, choices=TRABAJO_CHOICES)
  departamento = models.ForeignKey(Departamentos, on_delete=models.CASCADE)
  # image = models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)
  habilidades = models.ManyToManyField(Habilidades)
  descripcion = RichTextField()


  def __str__(self): 
    return (f'[{self.id}] {self.nombres} {self.apellidos} {self.profesion} {self.departamento}')

  class Meta:
    verbose_name = 'Empleado'
    verbose_name_plural = 'Empleados'