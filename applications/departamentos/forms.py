from django import forms

class NewDepartamentoForm(forms.Form):
  """NewDepartamentoForm definition."""

  # TODO: Define form fields here
  nombres_empleado = forms.CharField(max_length=50, required=True)
  apellidos_empleado = forms.CharField(max_length=50, required=True)
  nombre_departamento = forms.CharField(max_length=50, required=True)
  nombre_corto_departamento = forms.CharField(max_length=20, required=True)