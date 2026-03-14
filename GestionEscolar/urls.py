from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.base , name="base"),
    path('admin/', admin.site.urls, name="admin"),
    path('alumnos/', include('alumnos.urls')),
    path('cursos/', include('cursos.urls')),
    path('profesores/', include('profesores.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('sobre_nosotros/', views.sobre_nosotros, name="sobre_nosotros"),
    path('contacto/', views.contacto, name="contacto"),
    path('ayuda/', views.ayuda, name="ayuda"),
    path('terminos/', views.terminos, name="terminos"),
    path('reglamento/', views.reglamento, name="reglamento"),
    path('directorio_docente/', views.directorio_docente, name="directorio_docente"),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
]

# Configuración de errores
handler404 = 'GestionEscolar.views.error_404'
handler500 = 'GestionEscolar.views.error_500'