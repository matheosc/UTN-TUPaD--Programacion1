# EJERCICIO 7

asistencias = ["Ana", "Luis", "Ana", "María", "Luis", "Pedro", "Ana"]
cant_asistencias = {}
presentes = set(asistencias)
print("Lista Original:")
print(asistencias)
print("Lista sin repetidos: ")
print(presentes)

for e in asistencias:
    if e not in cant_asistencias.keys():
        cant_asistencias[e] = 1
    else:
        cant_asistencias[e] += 1

print("Cantidad de veces que asistieron:")
print(cant_asistencias)
