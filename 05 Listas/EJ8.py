# EJERCICIO 8

# 8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
# ● Mostrar el promedio de cada estudiante.
# ● Mostrar el promedio de cada materia.

notas = [[5, 8, 7],[3, 5, 1],[7, 4, 8],[2, 7, 6],[8, 7, 10]]
print(notas)
promedios_alum = []
promedios_mat = []
acum_mat = [0, 0, 0]
acum = 0

for a in range(5):
    for i in range(3):
        acum += notas[a][i]
        acum_mat[i] += notas[a][i]
    promedios_alum.append(acum/3)
    acum = 0
    print(f"El promedio del alumno N.{a+1} es de {promedios_alum[a]:.2f}")

for i in range(3):
    promedios_mat.append(acum_mat[i]/5)
    print(f"El promedio de la materia N.{i+1} es de {promedios_mat[i]:.2f}")