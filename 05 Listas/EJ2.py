# EJERCICIO 2

# 2) Pedir al usuario que cargue 5 productos en una lista.
# ● Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# ● Preguntar al usuario qué producto desea eliminar y actualizar la lista.

lista_productos = []

while len(lista_productos) < 5:
    producto = input("Por favor ingrese un producto a agregar a la lista: ").capitalize()
    lista_productos.append(producto)

print(sorted(lista_productos))

prod_eliminar = input("Que producto desea eliminar? ").capitalize()

if prod_eliminar in lista_productos:
    lista_productos.remove(prod_eliminar)
else:
    print("No se encontro el producto indicado en la lista, remocion omitida.")
    
print(sorted(lista_productos))