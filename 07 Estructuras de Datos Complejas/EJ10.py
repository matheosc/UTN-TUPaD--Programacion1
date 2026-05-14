# EJERCICIO 10

invertido = {}

original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago"
    }

print("Diccionario original:")
print(original)

for e in original.keys():
    invertido[original[e]] = e

print("Diccionario invertido:")
print(invertido)