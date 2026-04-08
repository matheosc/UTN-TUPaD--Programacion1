# EJERCICIO 6

# 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha
# (el último pasa a ser el primero).

import random

lista = []

for i in range(7):
    lista.append(random.randint(0, 100))
print(lista)

ultimo = lista[len(lista)-1]

lista.pop()

lista.insert(0, ultimo)

print("==============")
print(lista)