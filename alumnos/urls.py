from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='portal_alumnos'),
    path('lista/', views.lista_alumnos, name='lista_alumnos'),
    path('agregar/', views.agregar_alumno, name='agregar_alumno'),
]