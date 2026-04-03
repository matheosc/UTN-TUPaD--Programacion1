# EJERCICIO 1

# 1) Crear una lista con las notas de 10 estudiantes.
# ● Mostrar la lista completa.
# ● Calcular y mostrar el promedio.
# ● Indicar la nota más alta y la más baja.

notas = [3, 5, 10, 9, 8, 9, 9, 4, 7, 6]
suma_total = 0
mayor = 0
menor = 99

for i in range(10):
    suma_total += notas[i]
    print(f"El alumno N{i+1} tiene una nota de {notas[i]}")
    mayor = notas[i] if mayor < notas[i] else mayor 
    menor = notas[i] if menor > notas[i] else menor

promedio = suma_total / len(notas)
print(f"El promedio de las notas es de: {promedio}")
print(f"La nota mas baja es: {menor}")
print(f"La nota mas alta es: {mayor}")