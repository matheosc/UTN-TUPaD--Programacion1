# EJERCICIO 4

numeros_contactos = {}

def validar_nombre(nombre):
    while not nombre.isalpha():
        nombre = input("Error, por favor ingrese un nombre válido: ").strip().capitalize()
    return nombre

def validar_numero(numero):
    while not numero.isdigit():
        numero = input("Error, por favor ingrese un numero valido: ").strip()
    return numero

for i in range(5):
    nombre = validar_nombre(input("Ingresa un nombre: ").strip().capitalize())
    numero = int(validar_numero(input("Ingresa el numero del contacto: ")).strip())

    numeros_contactos[nombre] = numero

nombre_buscar = input("Ingrese el nombre del contacto a buscar: ")

if nombre_buscar in numeros_contactos.keys():
    print(f"El numero del contacto '{nombre_buscar}' es {numeros_contactos[nombre_buscar]}")
else:
    print("El contacto no existe.")

