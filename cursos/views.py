from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def inicio(request):
    return render(request, 'cursos/inicio.html')

@login_required
def lista_alumnos(request):
    return render(request, 'cursos/lista_cursos.html', {'lista_alumnos': []})

@login_required
def agregar_alumno(request):
    return render(request, 'cursos/agregar_curso.html')