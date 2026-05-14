# EJERCICIO 5

palabras = set()
cant_palabras = {}

frase = input("Ingrese una frase: ")

for palabra in frase.split():
    palabras.add(palabra.capitalize())
    if palabra.capitalize() not in cant_palabras.keys():
        cant_palabras[palabra.capitalize()] = 1
    else:
        cant_palabras[palabra.capitalize()] += 1

print(f"Las palabras unicas son: {palabras}")
print(f"Las cantidades de cada palabra son: {cant_palabras}")