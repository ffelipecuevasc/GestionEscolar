from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from profesores.models import Profesor
from profesores.forms import ProfesorForm

@login_required
def inicio(request):
    return render(request, 'profesores/inicio.html')

@login_required
def lista_profesores(request):
    profesores = Profesor.objects.all()
    contexto = {'lista_profesores': profesores}
    return render(request, 'profesores/lista_profesores.html', contexto)

@login_required
def agregar_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_profesores')
    else:
        form = ProfesorForm()
    contexto = {'form': form}
    return render(request, 'profesores/agregar_profesor.html', contexto)