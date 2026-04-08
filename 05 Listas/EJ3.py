#  EJERCICIO 3

# 3) Generar una lista con 15 números enteros al azar entre 1 y 100.
# ● Crear una lista con los pares y otra con los impares.
# ● Mostrar cuántos números tiene cada lista.

import random

lista = []
for i in range(15):
    lista.append(random.randint(1, 100))

lista_par = []
lista_impar = []

for i in range(len(lista)):
    if lista[i] % 2 == 0:
        lista_par.append(lista[i])
    else:
        lista_impar.append(lista[i])

print(f"Lista: {lista} . Tiene {len(lista)} elementos")
print(f"Lista par: {lista_par} . Tiene {len(lista_par)} elementos")
print(f"Lista impar: {lista_impar} . Tiene {len(lista_impar)} elementos")