# 6) Escribir un programa que solicite al usuario el consumo mensual de energía eléctrica en
# kilovatios (kWh) e indique la categoría del consumo según el siguiente criterio:
# • Menor que 150 kWh: “Consumo bajo”.
# • Entre 150 y 300 kWh (inclusive): “Consumo medio”.
# • Mayor que 300 kWh: “Consumo alto”.
# Además, si el consumo supera los 500 kWh, mostrar un mensaje adicional que diga:
# “Considere medidas de ahorro energético”.
# El programa debe imprimir por pantalla la categoría correspondiente.

consumo = int(input("Ingrese el consumo mensual en kWh: "))

if (consumo < 150):
    print("Consumo bajo")
elif (consumo <= 300):
    print("Consumo medio")
elif (consumo > 300):
    print("Consumo alto")

if (consumo > 500):
    print("Considere medidas de ahorro energético")

