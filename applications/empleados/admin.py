from django.contrib import admin
from .models import Empleados, Habilidades

# Register your models here.

class EmpleadosAdmin(admin.ModelAdmin):
  list_display = (
    'nombres',
    'apellidos',
    'profesion',
    'departamento',
  )

  search_fields = ('nombres', 'apellidos',)
  list_filter = ('profesion', 'habilidades',)
  filter_horizontal = ('habilidades',)

admin.site.register(Empleados, EmpleadosAdmin)
admin.site.register(Habilidades)