# Requisitos
# 1. Pedir nombre del cliente (solo letras, validar con .isalpha() en while). check
# 2. Pedir cantidad de productos a comprar (número entero positivo, validar con .isdigit() en while). check
# 3. Por cada producto (usar for):
#       o Pedir precio (entero, validar .isdigit()). check
#       o Pedir si tiene descuento S/N (validar con while, aceptar S o N en cualquier mayuscula/minuscula). check
#       o Si tiene descuento: aplicar 10% al precio de ese producto. check
# 4. Al final mostrar:
#       o Total sin descuentos
#       o Total con descuentos
#       o Ahorro total
#       o Promedio por producto (usar float y formatear con .2f)

# Salida esperada (ejemplo)
# Cliente: Ana
# Cantidad de productos: 3
# Producto 1 - Precio: 100 Descuento (S/N): s
# Producto 2 - Precio: 50 Descuento (S/N): n
# Producto 3 - Precio: 200 Descuento (S/N): s
# Total sin descuentos: $350
# Total con descuentos: $320.00
# Ahorro: $30.00
# Promedio por producto: $106.67

total_desc = 0
total = 0
ahorro = 0
promed = 0

nombre = input("Cliente: ")

while not nombre.isalpha():
    nombre = input("Por favor, ingrese un nombre valido (solo letras): ")

cantidad_prod = input("Cantidad de productos: ")

while not cantidad_prod.isdigit():
    cantidad_prod = input("Por favor, ingrese una cantidad de productos valida")

cantidad_prod = int(cantidad_prod)

for i in range(cantidad_prod):
    precio = input(f"Producto {i+1} - Precio : ")
    while not precio.isdigit():
        precio = input("Por favor ingrese un numero entero: ")
    
    precio = int(precio)
    total += precio
    
    tiene_desc = input("El producto tiene descuento? (S/N): ").upper()
    if  tiene_desc == 'S':
        total_desc += precio * 0.9
        ahorro += precio * 0.1
    else:
        total_desc += precio

promed = total_desc / cantidad_prod

print(f"""Total sin descuentos: {total}
Total con descuentos: {total_desc}
Ahorro: {ahorro}
Promedio por producto: {promed:.2f}""")

