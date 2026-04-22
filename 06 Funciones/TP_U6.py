# EJERCICIO 1

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

# EJERCICIO 2

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

nombre = input("Ingrese su nombre: ")

saludar_usuario(nombre)

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

# EJERCICIO 4
import math

def calcular_area_circulo(radio):
    return(math.pi* (radio**2))

def calcular_perimetro_circulo(radio):
    return(2*math.pi*radio)

radio = int(input("Por favor ingrese el radio del circulo: "))

print(f"El area del circulo es de: {calcular_area_circulo(radio):.2f}")
print(f"El perimetro del circulo es de: {calcular_perimetro_circulo(radio)}")

# EJERCICIO 5

def segundos_a_hora(segundos):
    return segundos/3600

segundos = int(input("Ingrese la cantidad de segundos a transformar en horas: "))

print(f"Los {segundos} segundos son equivalentes a {segundos_a_hora(segundos)} hora/s")

# EJERCICIO 6

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero*i}")
    
numero = int(input("Ingrese un numero para mostrar su tabla de multiplicacion: "))

tabla_multiplicar(numero)

# EJERCICIO 7

def operaciones_basicas(a, b)-> tuple:
    return (a+b, a-b, a*b, a/b)

num_a = int(input("Ingrese un numero: "))
num_b = int(input("Ingrese otro numero: "))

suma, resta, mult, divi = operaciones_basicas(num_a, num_b)

print(f"""
Sumados = {suma}
Restados = {resta}
Multiplicados = {mult}
Divididos = {divi}
""")

# EJERCICIO 8
peso_usuario = "a"
alt_usuario = "a"

def calcular_imc(peso, altura):
    return peso / (altura**2)

peso_usuario = input("Ingrese su peso en gramos: ")
while not peso_usuario.isdigit():
    peso_usuario = input("Error, ingrese su peso en gramos: ")
peso_usuario = float(peso_usuario)/1000

alt_usuario = input("Ingrese su altura en centímetros: ")
while not alt_usuario.isdigit():
    alt_usuario = input("Error, ingrese su altura en centímetros: ")
alt_usuario = float(alt_usuario)/100

print(f"Su IMC es de: {calcular_imc(peso_usuario, alt_usuario):.2f}")

# EJERCICIO 9

def celsius_a_fahrenheit(celsius):
    return (celsius*9/5)+32

temp_cel = input("Por favor ingrese una temperatura en Celsius: ")

while not temp_cel.isdigit():
    temp_cel = input("Error, ingrese una temperatura en Celsius: ")
temp_cel = float(temp_cel)

print(f"La temperatura de {temp_cel}° Celsius es equivalente a {celsius_a_fahrenheit(temp_cel)}° Fahrenheit")

# EJERCICIO 10

def calcular_promedio(a, b, c):
    return (a+b+c)/3

def verif_num(caracter):
    while not caracter.isdigit():
        caracter = input("Error, ingrese una entrada valida: ")
    return caracter

num_a = int(verif_num(input("Por favor ingrese un numero: ")))
num_b = int(verif_num(input("Por favor ingrese otro numero: ")))
num_c = int(verif_num(input("Por favor ingrese el ultimo numero: ")))

print(f"El promedio de los numeros ingresados es de: {calcular_promedio(num_a, num_b, num_c):.2f}")

