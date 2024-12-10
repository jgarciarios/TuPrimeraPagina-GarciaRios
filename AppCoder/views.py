from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import EstudianteForm, ProfesorForm, CursoForm, EntregableForm, UserRegistrationForm
from .models import Curso, Camada
from django.db import migrations
from .forms import CamadaForm


def crear_camada(request):
    if request.method == 'POST':
        form = CamadaForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('home')  
    else:
        form = CamadaForm()

    return render(request, 'buscar_camada.html', {'form': form})

def add_column(apps, schema_editor):
    schema_editor.execute('ALTER TABLE AppCoder_camada ADD COLUMN numero_camada CHAR(100);')

class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', 'previous_migration_name'),
    ]

    operations = [
        migrations.RunPython(add_column),
    ]

def profile(request):
    return render(request, 'profile.html')  



def home(request):
    return render(request, 'AppCoder/home.html')

def handle_form(request, form_class, template_name, redirect_url):
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(redirect_url)
    else:
        form = form_class()
    return render(request, template_name, {'form': form})

def agregar_estudiante(request):
    return handle_form(request, EstudianteForm, 'AppCoder/agregar_estudiante.html', '/AppCoder/home/')

def agregar_profesor(request):
    return handle_form(request, ProfesorForm, 'AppCoder/agregar_profesor.html', '/AppCoder/home/')

def agregar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('/AppCoder/home/') 
    else:
        form = CursoForm()
        pass

    return render(request, 'AppCoder/agregar_curso.html')

def agregar_entregable(request):
    return handle_form(request, EntregableForm, 'AppCoder/agregar_entregable.html', '/AppCoder/home/')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next', '/AppCoder/home/')
                return redirect(next_url)  # Redirige a la página de inicio o la URL 'next'
            else:
                form.add_error(None, "Usuario o contraseña incorrectos")
    else:
        form = AuthenticationForm()
    return render(request, 'AppCoder/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/AppCoder/home/')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/AppCoder/home/')
    else:
        form = UserRegistrationForm()
    return render(request, 'AppCoder/register.html', {'form': form})
