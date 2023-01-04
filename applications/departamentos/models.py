from django.db import models

# Create your models here.

class Departamentos(models.Model):
  nombre = models.CharField('Nombre', max_length=50)
  nombre_corto = models.CharField('Nombre corto', max_length=20)
  activo = models.BooleanField('Activo', default=True, )

  def __str__(self):
    return (f'[{self.id}] Nombre: {self.nombre}, Nombre corto: {self.nombre_corto}, Activo: {self.activo}')

  class Meta: 
    verbose_name = 'Departamento'
    verbose_name_plural = 'Departamentos'