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