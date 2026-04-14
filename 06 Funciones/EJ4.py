# EJERCICIO 4
import math

def calcular_area_circulo(radio):
    print(math.pi* (radio**2))

def calcular_perimetro_circulo(radio):
    print(2*math.pi*radio)

radio = int(input("Por favor ingrese el radio del circulo: "))

calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)