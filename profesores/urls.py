from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='portal_profesores'),
    path('lista/', views.lista_alumnos, name='lista_profesores'),
    path('agregar/', views.agregar_alumno, name='agregar_profesor'),
]