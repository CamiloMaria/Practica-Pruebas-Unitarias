from EstudianteProfesor import Estudiante, Profesor
import unittest

class TestEstudiante(unittest.TestCase):
    def setUp(self):
        self.e1 = Estudiante("Ana Martínez")
        self.e2 = Estudiante("Pedro García")
        self.p1 = Profesor("Juan Pérez")

    def test_inscribirse(self):
        # Comprobamos que se inscribe correctamente en una asignatura
        self.e1.inscribirse("Matemáticas")
        self.assertIn("Matemáticas", self.e1.asignaturas)

class TestProfesor(unittest.TestCase):
    def setUp(self):
        self.p1 = Profesor("Juan Pérez")
        self.e1 = Estudiante("Ana Martínez")
        self.e2 = Estudiante("Pedro García")
    
    def test_publicar_nota(self):
        # Publicamos algunas notas para los estudiantes
        self.p1.publicar_nota(self.e1, "Matemáticas", 9)
        self.p1.publicar_nota(self.e1, "Física", 7)
        self.p1.publicar_nota(self.e2, "Matemáticas", 8)
        self.p1.publicar_nota(self.e2, "Química", 10)
        
        # Comprobamos que las notas se han publicado correctamente
        self.assertEqual(self.e1.notas["Matemáticas"], 9)
        self.assertEqual(self.e1.notas["Física"], 7)
        self.assertEqual(self.e2.notas["Matemáticas"], 8)
        self.assertEqual(self.e2.notas["Química"], 10)

if _name_ == '_main_':
        TestEstudiante()
        TestProfesor()
