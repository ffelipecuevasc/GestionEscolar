from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cursos.models import Curso
from cursos.forms import CursoForm

@login_required
def inicio(request):
    return render(request, 'cursos/inicio.html')

@login_required
def lista_cursos(request):
    cursos = Curso.objects.select_related('profesor').all()
    contexto = {'lista_cursos': cursos}
    return render(request, 'cursos/lista_cursos.html', contexto)

@login_required
def agregar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_cursos')
    else:
        form = CursoForm()
    contexto = {'form': form}
    return render(request, 'cursos/agregar_curso.html', contexto)