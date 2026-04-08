# EJERCICIO 10

# 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# ● Mostrar el total vendido por cada producto. ventas_prod
# ● Mostrar el día con mayores ventas totales.  sum_dia
# ● Indicar cuál fue el producto más vendido en la semana.  max_p

ventas = [
    [12, 87, 45, 23, 91, 34, 56],
    [78, 11, 69, 50, 32, 99, 4],
    [27, 63, 8, 74, 41, 55, 90],
    [36, 22, 95, 60, 13, 48, 71]
]

sum_dia = [0, 0, 0, 0, 0, 0, 0]
ventas_prod = [0, 0, 0, 0]
max_p = 0
pos_p = 0
max_d = 0
pos_d = 0

for p in range(4):
    for d in range(7):
        ventas_prod[p] += ventas[p][d]
        sum_dia[d] += ventas[p][d]
        
for i in range(4):
    print(f"El producto N.{i+1} se vendio un total de {ventas_prod[i]} veces.")
    if max_p < ventas_prod[i]:
        max_p = ventas_prod[i]
        pos_p = i

print(f"El producto mas vendido fue el N.{pos_p+1}")

for i in range(7):
    if max_d < sum_dia[i]:
        max_d = sum_dia[i]
        pos_d = i

print(f"El dia con mas ventas totales fue el dia N.{pos_d+1}")