# EJERCICIO 13

# 13) Dada la siguiente lista de puntajes de un videojuego:
# puntajes = [450, 1200, 875, 990, 300, 1500, 640]
# ● Mostrar el puntaje más alto y el más bajo.
# ● Mostrar la lista ordenada de mayor a menor (ranking).
# ● Indicar en qué posición del ranking se encuentra el puntaje 990.

puntajes = [450, 1200, 875, 990, 300, 1500, 640]

min = sorted(puntajes)[0]
max = sorted(puntajes)[-1]

print(f"El puntaje mas bajo es de {min} y el mas alto es de {max}")
print(sorted(puntajes))
print(f"El puntaje 990 se encuentra en la posicion {puntajes.index(990)+1}")