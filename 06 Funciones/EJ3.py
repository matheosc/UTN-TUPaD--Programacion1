# EJERCICIO 3

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

def validar_string(dato):
    while not dato.isalpha():
        dato = input("Ingreso un dato invalido, por favor intente nuevamente: ")
    return dato

nombre = validar_string(input("Ingrese su nombre: "))
apellido = validar_string(input("Ingrese su apellido: "))
edad = input("Ingrese su edad: ")
while not edad.isdigit():
    edad = input("Ingreso un dato invalido, por favor intente nuevamente: ")
residencia = validar_string(input("Ingrese su lugar de residencia: "))

informacion_personal(nombre, apellido, edad, residencia)
