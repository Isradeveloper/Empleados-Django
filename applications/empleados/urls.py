from django.urls import path
from . import views

urlpatterns = [
    path('listar_todos_empleados/', views.ListAllEmpleados.as_view()),
]