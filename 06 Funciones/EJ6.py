# EJERCICIO 6

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero*i}")
    
numero = int(input("Ingrese un numero para mostrar su tabla de multiplicacion: "))

tabla_multiplicar(numero)