from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='portal_cursos'),
    path('lista/', views.lista_alumnos, name='lista_cursos'),
    path('agregar/', views.agregar_alumno, name='agregar_curso'),
]