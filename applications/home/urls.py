from django.urls import path
from . import views

app_name = 'home_app'

urlpatterns = [
    path('home/', views.IndexView.as_view()),
    path('lista/', views.PruebaListView.as_view()),
    path('lista_prueba/', views.ModeloListView.as_view()),
    path('prueba/add/', views.PruebaCreateView.as_view(), name='agregar'),
    path('prueba/success/', views.SuccessView.as_view(), name='success')
]