from EstudianteProfesor import Estudiante, Profesor

def main():
    p1 = Profesor("Juan Pérez")

    # Creamos dos estudiantes
    e1 = Estudiante("Ana Martínez")
    e2 = Estudiante("Pedro García")

    # Añadimos a los estudiantes a la lista de estudiantes del profesor
    p1.estudiantes.append(e1)
    p1.estudiantes.append(e2)

    # Inscribimos a los estudiantes en algunas asignaturas
    e1.inscribirse("Matemáticas")
    e1.inscribirse("Física")
    e2.inscribirse("Matemáticas")
    e2.inscribirse("Química")

    # Publicamos algunas notas para los estudiantes
    p1.publicar_nota(e1, "Matemáticas", 9)
    p1.publicar_nota(e1, "Física", 7)
    p1.publicar_nota(e2, "Matemáticas", 8)
    p1.publicar_nota(e2, "Química", 10)

    # Mostramos las notas de los estudiantes
    print("Notas de Ana Martínez:")
    e1.ver_notas()
    print("Notas de Pedro García:")
    e2.ver_notas()

if __name__ == '__main__':
        main()