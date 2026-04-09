# EJERCICIO 12

# 12) Pedir al usuario que ingrese 8 números enteros y almacenarlos en una lista.
# ● Mostrar la lista original.
# ● Mostrar la lista ordenada de menor a mayor.
# ● Mostrar la lista ordenada de mayor a menor.
# ● Investigar el uso de sorted() y del parámetro reverse.

lista_enteros = []

for i in range(8):
    numero = input("Ingrese un numero entero: ")
    while not numero.isdigit():
        numero = input("Error, ingrese un numero valido: ")
    numero = int(numero)
    lista_enteros.append(numero)

print(lista_enteros)
print(sorted(lista_enteros))
print(sorted(lista_enteros, reverse=True))

