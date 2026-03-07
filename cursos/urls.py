from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='portal_cursos'),
    path('lista/', views.lista_cursos, name='lista_cursos'),
    path('agregar/', views.agregar_curso, name='agregar_curso'),
]