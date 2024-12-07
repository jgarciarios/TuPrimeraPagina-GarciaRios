from django.shortcuts import render, get_object_or_404
from .models import Estudiante, Profesor, Curso, Entregable
from django.http import HttpResponse

def index(request):
    return HttpResponse("¡Bienvenido a AppCoder!")

def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'AppCoder/estudiantes_list.html', {'estudiantes': estudiantes})

def detalle_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    return render(request, 'AppCoder/estudiante_detail.html', {'estudiante': estudiante})
