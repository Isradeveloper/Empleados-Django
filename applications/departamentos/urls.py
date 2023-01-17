from django.urls import path

from . import views

app_name = 'departamentos_app'

urlpatterns = [
  path('departamentos/add/', views.NewDepartamentoView.as_view(), name='add'),
  path('departamentos/success-add/', views.SuccessAdd.as_view(), name='success-add'),
  path('departamentos/ver/<pk>/', views.DepartamentosDetailView.as_view(), name='ver'),
  path('departamentos/all/', views.DepartamentosListView.as_view(), name='all')
]