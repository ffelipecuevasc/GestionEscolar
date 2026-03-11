from django.shortcuts import render, redirect, get_object_or_404 # Función para ocupar el template 404 personalizado
from django.contrib.auth.decorators import login_required
from alumnos.models import Alumno
from alumnos.forms import AlumnoForm

@login_required
def inicio(request):
    return render(request, 'alumnos/inicio.html')

@login_required
def lista_alumnos(request):
    # Acá se ejecuta un "SELECT * FROM alumnos_alumno"
    alumnos = Alumno.objects.all()
    contexto = {'lista_alumnos': alumnos}
    return render(request, 'alumnos/lista_alumnos.html', contexto)

@login_required
def agregar_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_alumnos')
    else:
        form = AlumnoForm()
    contexto = {'form': form}
    return render(request, 'alumnos/agregar_alumno.html', contexto)