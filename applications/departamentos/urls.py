from django.urls import path

from . import views

app_name = 'departamentos'

urlpatterns = [
  path('departamentos/add/', views.NewDepartamentoView.as_view(), name='add'),
  path('departamentos/success-add/', views.SuccessAdd.as_view(), name='success-add')
]