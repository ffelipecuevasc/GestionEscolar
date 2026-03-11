from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from alumnos.models import Alumno
from profesores.models import Profesor
from cursos.models import Curso
@login_required
def base(request):
    total_alumnos = Alumno.objects.count()
    total_profesores = Profesor.objects.count()
    total_cursos = Curso.objects.count()

    contexto = {
        'total_alumnos' : total_alumnos,
        'total_profesores' : total_profesores,
        'total_cursos' : total_cursos
    }
    return render(request, 'base.html', contexto)

def sobre_nosotros(request):
    return render(request, 'complementos_login/sobre_nosotros.html')
def contacto(request):
    return render(request, 'complementos_login/contacto.html')
def ayuda(request):
    return render(request, 'complementos_login/ayuda.html')
def terminos(request):
    return render(request, 'complementos_login/acce_politicas_terminos.html')
@login_required
def reglamento(request):
    return render(request, 'complementos_base/reglamento.html')
@login_required
def directorio_docente(request):
    return render(request, 'complementos_base/directorio_docente.html')


# ==========================================
# GESTIÓN DE ERRORES HTTP
# ==========================================

def error_404(request, exception):
    return render(request, 'errors/404.html', status=404)

def error_500(request):
    return render(request, 'errors/500.html', status=500)