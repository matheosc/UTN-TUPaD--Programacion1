# Actividad 1
print("Hola Mundo!")

# Actividad 2
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

# Actividad 3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su pais de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Actividad 4
import math

PI = 3.1416

radio = int(input("Ingrese el radio del circulo: "))
area = radio**2 * math.pi  # o usar variable PI para un resultado mas corto
perimetro = 2*math.pi*radio

print(f"El circulo de radio {radio} tiene un area de {area} y su perimetro es de {perimetro}")

# Actividad 5
segundos = int(input("Ingrese una cantidad de segundos: "))

horas = segundos // 3600

print(f"Esa cantidad de segundos equivale a {horas} hora/s.")

# Actividad 6
numero = int(input("Ingrese un numero: "))

print(f"La tabla de {numero} es:")

print(f"{numero} x 1 = {numero}")
print(f"{numero} x 2 = {numero*2}")
print(f"{numero} x 3 = {numero*3}")
print(f"{numero} x 4 = {numero*4}")
print(f"{numero} x 5 = {numero*5}")
print(f"{numero} x 6 = {numero*6}")
print(f"{numero} x 7 = {numero*7}")
print(f"{numero} x 8 = {numero*8}")
print(f"{numero} x 9 = {numero*9}")
print(f"{numero} x 10 = {numero*10}")

# Actividad 7
num_uno = int(input("Ingrese un numero entero distinto de cero: "))
num_dos = int(input("Ingrese otro numero entero distinto de cero: "))

suma = num_uno + num_dos
resta = num_uno - num_dos
mult = num_uno * num_dos
div = num_uno / num_dos

print("La suma de los numeros es: ", suma)
print("La resta de los numeros es: ", resta)
print("La multiplicación de los numeros es: ", mult)
print("La división de los numeros es: ", div)

# Actividad 8
peso = float(input("Ingrese su peso en kg separando decimales con un punto (ejemplo: 70.3kg): "))
altura = float(input("Ingrese su altura en m separando decimales con un punto (ejemplo: 1.75m): "))

IMC = peso / altura**2

print("Su indice de masa corporal es de:", IMC)

# Actividad 9
temp_cels = int(input("Ingrese la temperatura en grados Celsius: "))

temp_far = 9/5*temp_cels+32

print(f"El equivalente de {temp_cels} grados Celsius en escala Farenheit es de {temp_far} ")

# Actividad 10
num_uno = float(input("Ingrese un numero: "))
num_dos = float(input("Ingrese otro numero: "))
num_tres = float(input("Ingrese un ultimo numero: "))

prom = (num_uno + num_dos + num_tres) / 3

print(f"El promedio de los numeros ingresados es de: {prom}")