import math

PI = 3.1416

radio = int(input("Ingrese el radio del circulo: "))
area = radio**2 * math.pi  # o usar variable PI para un resultado mas corto
perimetro = 2*math.pi*radio

print(f"El circulo de radio {radio} tiene un area de {area} y su perimetro es de {perimetro}")