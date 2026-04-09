# EJERCICIO 11

    # 11) Crear una lista con los nombres de 10 estudiantes.
    # ● Solicitar al usuario que ingrese un nombre a buscar.
    # ● Indicar si el nombre se encuentra en la lista.
    # ● Mostrar la posición en la que aparece.
    # ● Si no se encuentra, informar que no está en la lista.

lista_estudiantes = [
    "Sofia",
    "Mateo",
    "Valentina",
    "Lucas",
    "Martina",
    "Benjamín",
    "Camila",
    "Joaquín",
    "Lucía",
    "Santiago"
    ]

pos_nombre = -1          # Soy consciente que no deberia mezclar tipos de datos con verificaciones pero considero que es un ejercicio corto y simple

nombre = input("Ingrese un nombre a buscar: ").strip().capitalize()
while not nombre.isalpha():
    nombre = input("Error, ingrese un nombre valido: ").strip().capitalize()

for i in range(len(lista_estudiantes)):
    if lista_estudiantes[i] == nombre:
        pos_nombre = i
    
if pos_nombre != -1:
    print(f"El nombre se encuentra en la posicion {pos_nombre+1}")
else:
    print("El nombre que ingreso no se encuentra en la lista")