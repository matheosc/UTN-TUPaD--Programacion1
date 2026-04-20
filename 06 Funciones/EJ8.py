# EJERCICIO 8
peso_usuario = "a"
alt_usuario = "a"

def calcular_imc(peso, altura):
    return peso / (altura**2)

peso_usuario = input("Ingrese su peso en kilogramos: ")
while not peso_usuario.isdigit():
    peso_usuario = input("Error, ingrese su peso en kilogramos: ")
peso_usuario = float(peso_usuario)

alt_usuario = input("Ingrese su altura en metros: ")
while not isinstance(alt_usuario, float):
    alt_usuario= input("Error, ingrese su altura en metros: ")
alt_usuario = float(alt_usuario)

print(f"Su IMC es de: {calcular_imc(peso_usuario, alt_usuario):.2f}")