from django import forms
from .models import Prueba

class PruebaForm(forms.ModelForm):
  """Form definition for Prueba."""

  class Meta:
    """Meta definition for Pruebaform."""

    model = Prueba

    # Campos
    fields = (
      'titulo',
      'subtitulo',
    )

    # Personalización
    widgets = {
      'titulo': forms.TextInput(
        attrs = {
          'placeholder': 'Ingresa el título',
          'class': 'titulo'
        }
      )
    }

# Validaciones de campos
  def clean_subtitulo(self):
    subtitulo = self.cleaned_data.get('subtitulo')
    # subtitulo = self.cleaned_data['subtitulo']

    # TODO Validation
    if len(subtitulo) < 10:
      raise forms.ValidationError('Debes ingresar más de 10 carácteres')
  
    return subtitulo

