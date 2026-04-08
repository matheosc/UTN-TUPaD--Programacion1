# EJERCICIO 5

# 5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
# ● Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# ● Mostrar la lista final actualizada.

lista_estudiantes = ["Luis", "Jose", "Mario", "Nicolas", "Noelia", "Melina", "Agustina", "Delfina"]
print(lista_estudiantes)

respuesta = input("Desea agregar un nuevo estudiante o eliminar uno existente? (A:Agregar / E:Eliminar): ").upper()

if respuesta == 'A':
    nombre_nuevo = input("Por favor ingrese el nombre del estudiante para agregar a la lista: ")
    while not nombre_nuevo.isalpha() :
        nombre_nuevo = input("Error, ingrese un nombre valido: ")
    lista_estudiantes.append(nombre_nuevo.capitalize())
elif respuesta == 'E':
    nombre_eliminar = input("Por favor ingrese el nombre del estudiante a quitar de la lista: ")
    while not nombre_eliminar.isalpha() :
        nombre_eliminar = input("Error, ingrese un nombre valido: ")
    if nombre_eliminar in lista_estudiantes:
        lista_estudiantes.remove(nombre_eliminar.capitalize())
    else:
        print("Error, no existe estudiante que se llame asi en la lista.")
else:
    print("Error, ingreso una opcion invalida.")

print(f"La lista queda de la siguiente forma: {lista_estudiantes}")