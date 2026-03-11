from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='portal_profesores'),
    path('lista/', views.lista_profesores, name='lista_profesores'),
    path('agregar/', views.agregar_profesor, name='agregar_profesor'),
]