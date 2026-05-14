# EJERCICIO 6

alumnos = {}
notas = []

for i in range(3):
    nombre_alumno = input("Ingrese el nombre del alumno: ")
    for n in range(3):
        nota_alumno = int(input("Ingrese una nota del alumno: "))
        notas.append(nota_alumno)
    alumnos[nombre_alumno] = tuple(notas)
    notas = []

print(alumnos)
