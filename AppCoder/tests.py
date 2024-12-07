from django.test import TestCase
from .models import Estudiante

class EstudianteModelTest(TestCase):
    def test_create_estudiante(self):
        estudiante = Estudiante.objects.create(nombre="Juan", apellido="García", email="juan@correo.com")
        self.assertEqual(estudiante.nombre, "Juan")
        self.assertEqual(estudiante.apellido, "García")
        self.assertEqual(estudiante.email, "juan@correo.com")

