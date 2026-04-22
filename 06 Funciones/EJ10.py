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

