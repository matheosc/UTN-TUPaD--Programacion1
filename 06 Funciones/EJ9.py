# EJERCICIO 9

def celsius_a_fahrenheit(celsius):
    return (celsius*9/5)+32

temp_cel = input("Por favor ingrese una temperatura en Celsius: ")

while not temp_cel.isdigit():
    temp_cel = input("Error, ingrese una temperatura en Celsius: ")
temp_cel = float(temp_cel)

print(f"La temperatura de {temp_cel}° Celsius es equivalente a {celsius_a_fahrenheit(temp_cel)}° Fahrenheit")
