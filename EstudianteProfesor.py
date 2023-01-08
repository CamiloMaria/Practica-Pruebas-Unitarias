class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = {}
        self.asignaturas = []
    
    def inscribirse(self, asignatura):
        self.asignaturas.append(asignatura)
    
    def ver_notas(self):
        for asignatura, nota in self.notas.items():
            print(f"Asignatura: {asignatura}, Nota: {nota}")

class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []
    
    def publicar_nota(self, estudiante, asignatura, nota):
        estudiante.notas[asignatura] = nota

