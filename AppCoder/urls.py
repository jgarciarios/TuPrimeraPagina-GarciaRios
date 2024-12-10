from django.contrib import admin
from django.urls import path
from . import views
from django.urls import include

app_name = 'AppCoder'

urlpatterns = [
    path('', views.home, name='home'), 
    path('agregar_estudiante/', views.agregar_estudiante, name='agregar_estudiante'),
    path('agregar_profesor/', views.agregar_profesor, name='agregar_profesor'),
    path('agregar_curso/', views.agregar_curso, name='agregar_curso'),
    path('agregar_entregable/', views.agregar_entregable, name='agregar_entregable'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('admin/', admin.site.urls, name='admin'),
]
