# EJERCICIO 8

stock_productos = {}
seguir = True

while seguir:

    opcion = 9

    print("1. Consultar stock segun producto")
    print("2. Agregar unidades al stock")
    print("3. Agregar producto")
    print("0. Salir del sistema")
    opcion = int(input("Ingrese la opcion segun desee: "))

    match opcion:
        case 1:
            prod_buscar = input("Ingrese el nombre del producto: ").capitalize()
            if prod_buscar not in stock_productos.keys():
                print("Error. Ingreso un producto que no se encuentra en el sistema. Intente nuevamente")
            else:
                print(f"El producto {prod_buscar} tiene {stock_productos[prod_buscar]} unidades en existencia.")

        case 2:
            prod_buscar = input("Ingrese el nombre del producto: ").capitalize()
            if prod_buscar not in stock_productos.keys():
                print("Error. Ingreso un producto que no se encuentra en el sistema. Intente nuevamente")
            else:
                cant_cargar = int(input("Ingrese las unidades a cargar al stock: "))
                stock_productos[prod_buscar] += cant_cargar
                print(f"Se han agregado {cant_cargar} unidades exitosamente.")

        case 3:
            prod_cargar = input("Ingrese el nombre del producto a cargar: ").capitalize()
            if prod_cargar in stock_productos.keys():
                print("Error. Estas intentando cargar un producto que ya se encuentra en el sistema. Intenta con otro.")
            else: 
                stock_productos[prod_cargar] = 0
                print(f"Has agregado {prod_cargar} exitosamente.")

        case 0:
            seguir = False
            print("Saliendo del sistema.")

        case _:
            print("Error. Ingreso una opcion invalida. Intenta nuevamente.")