from django import forms
from .models import Estudiante, Profesor, Curso, Entregable
from django import forms
from django.contrib.auth.models import User
from .models import Camada
from django.shortcuts import redirect


class CamadaForm(forms.ModelForm):
    class Meta:
        model = Camada
        fields = ['numero_camada'] 



class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirmar Contraseña")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    # Validación para asegurar que las contraseñas coinciden
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'email']

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'email', 'profesion']

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'camada']

class EntregableForm(forms.ModelForm):
    class Meta:
        model = Entregable
        fields = ['nombre', 'fecha_entrega', 'entregado']
from django.shortcuts import render
from .forms import CamadaForm

def crear_camada(request):
    if request.method == 'POST':
        form = CamadaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nombre_de_la_vista_donde_rediriges')
    else:
        form = CamadaForm()
    
    return render(request, 'ruta_a_tu_template.html', {'form': form})
