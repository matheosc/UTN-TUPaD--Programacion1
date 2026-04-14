# EJERCICIO 5

def segundos_a_hora(segundos):
    return segundos/3600

segundos = int(input("Ingrese la cantidad de segundos a transformar en horas: "))

print(f"Los {segundos} segundos son equivalentes a {segundos_a_hora(segundos)} hora/s")