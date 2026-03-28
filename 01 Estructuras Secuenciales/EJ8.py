peso = float(input("Ingrese su peso en kg separando decimales con un punto (ejemplo: 70.3kg): "))
altura = float(input("Ingrese su altura en m separando decimales con un punto (ejemplo: 1.75m): "))

IMC = peso / altura**2

print("Su indice de masa corporal es de:", IMC)