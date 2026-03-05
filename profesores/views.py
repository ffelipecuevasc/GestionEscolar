from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def inicio(request):
    return render(request, 'profesores/inicio.html')

@login_required
def lista_alumnos(request):
    return render(request, 'profesores/lista_profesores.html', {'lista_alumnos': []})

@login_required
def agregar_alumno(request):
    return render(request, 'profesores/agregar_profesor.html')