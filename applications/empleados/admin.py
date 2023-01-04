from django.contrib import admin
from .models import Empleados, Habilidades

# Register your models here.

class EmpleadosAdmin(admin.ModelAdmin):
  list_display = (
    'nombres',
    'apellidos',
    'profesion',
    'departamento',
    'nombre_completo',
  )

  #
  def nombre_completo(self, obj):
    # Itera todos los objetos de la tabla 
    print(obj.nombres)
    return (f'{obj.nombres} {obj.apellidos}')
  #

  search_fields = ('nombres', 'apellidos',)
  list_filter = ('profesion', 'habilidades',)
  filter_horizontal = ('habilidades',)

admin.site.register(Empleados, EmpleadosAdmin)
admin.site.register(Habilidades)