# EJERCICIO 4

# Dada una lista con valores repetidos:
# ● Crear una nueva lista sin elementos repetidos.
# ● Mostrar el resultado.

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
lista = []

for i in datos:
    if i not in lista:
        lista.append(i)

print(lista)