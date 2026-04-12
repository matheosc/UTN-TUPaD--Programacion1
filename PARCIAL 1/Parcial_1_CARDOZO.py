# Alumno: Matheo Cardozo
# Parcial 1 / Programacion 1

herramientas = []
existencias = []
fin_sist = False

while not fin_sist:
    print("================================")
    print("SISTEMA DE CONTROL DE INVENTARIO")
    print("================================")

    opcion = input("""Por favor, ingrese la opcion segun desee:
1. Carga Inicial de Herramientas
2. Carga de Existencias
3. Visualizacion de Inventario
4. Consulta de Stock
5. Reporte de Agotados
6. Alta de Nuevo Producto
7. Actualizacion de Stock (Venta/Reposicion de Stock)
8. Salir
Opcion: """)
    
    while not opcion.isdigit():
        opcion = input("Error, por favor ingrese una opcion valida (1 - 8): ")
    opcion = int(opcion)

    match opcion:
        case 1:         # Carga inicial de herramientas

            cantidad = input("Ingrese la cantidad de herramientas a cargar: ")      # Se registra la cantidad de herramientas a cargar
            while not cantidad.isdigit():       # Captura entrada invalida
                cantidad = input("Error, por favor ingrese una cantidad valida: ")
            cantidad = int(cantidad)

            for i in range(cantidad):                                               # Segun la cantidad de herramientas a cargar
                herramienta = input("Por favor, ingrese el nombre de la herramienta a agregar al sistema: ").strip().capitalize()
                while not herramienta.isalpha():        # Vuelve a pedir el ingreso si la entrada es invalida
                    herramienta = input("Error, ingrese un nombre valido: ").strip().capitalize()
                while herramienta in herramientas:      # Vuelve a pedir otra herramienta si la ingresada ya se encuentra en el sistema
                    herramienta = input("Error, la herramienta ya se encuentra en el sistema. Por favor ingrese otra herramienta: ").strip().capitalize()
                herramientas.append(herramienta)        # Agrega a la lista de los nombres
                existencias.append(0)       # Inicializa la cantidad de la herramienta ingresada en 0
                print("Se ha cargado exitosamente al sistema!")

        case 2:         # Carga de existencias

            if len(herramientas)>0:     # Verifica que existan herramientas cargadas al sistema
                for i in range(len(herramientas)):      # Segun la cantidad de herramientas en la lista
                    cant_exist = input(f"Ingrese la cantidad de unidades de {herramientas[i]} a ingresar: ")
                    while not cant_exist.isdigit():     # Captura y vuelve a pedir cantidades en caso de que la entrada sea invalida
                        cant_exist = input("Error, ingrese una cantidad valida: ")
                    existencias[i] += int(cant_exist)
                    print(f"Se han agregado {cant_exist} unidades exitosamente!")
            else:
                print("Error. No hay herramientas cargadas al sistema.")

        case 3:         # Visualizacion de inventario

            if len(herramientas)>0:     # Verifica que hayan herramientas cargadas en la lista
                print("----------- INVENTARIO --------------")
                for i in range(len(herramientas)):      # Por cada herramienta en lista
                    print(f"| - Herramienta: {herramientas[i]} -> Stock: {existencias[i]}")
            else:
                print("Error. No hay herramientas cargadas al sistema.")
            
        case 4:         # Consulta de stock
            
            if len(herramientas)<1:     # Verifica que no hayan herramientas en lista
                print("Sistema vacio. Primero cargue herramientas.")
            else:
                busqueda = input("Ingrese el nombre de la herramienta a buscar: ")
                while not busqueda.isalpha():       # Captura de ingreso invalido
                    busqueda = input("Error, ingrese un nombre valido: ")
                busqueda = busqueda.strip().capitalize()
                if busqueda in herramientas:
                    print(f"Hay {existencias[herramientas.index(busqueda)]} unidades disponibles de {busqueda}.")
                else:
                    print(f"La herramienta {busqueda} no se encuentra dentro del sistema.")

        
        case 5:         # Reporte de agotados

            if 0 in existencias:        # Si hay ceros en la lista de existencias entonces imprime el reporte
                print("| HERRAMIENTAS SIN STOCK |")
                for i in range(len(existencias)):
                    if existencias[i] == 0:
                        print(f"Herramienta: {herramientas[i]} -> Stock: {existencias[i]}")
            else:
                print("No hay herramientas sin stock.")

        case 6:         # Alta de nuevo producto
            
            herramienta = input("Ingrese el nombre de la herramienta: ")
            cant_exist = input("Ingrese la cantidad de unidades a cargar de la herramienta: ")
            if not herramienta.isalpha():       
                print("Error, el nombre ingresado es invalido.")
            elif herramienta.strip().capitalize() in herramientas:
                print("Error, la herramienta ya se encuentra en el sistema.")
            elif not cant_exist.isdigit():
                print("Error, la cantidad de unidades ingresada es invalida.")
            else:
                herramientas.append(herramienta.strip().capitalize())
                existencias.append(int(cant_exist))
                print("Herramienta y stock actualizado exitosamente!")
        
        case 7:         # Actualizacion de stock (venta/ingreso)

            op_venta = input("Venta o Ingreso de mercadería? (V/I): ").strip().upper()      # Decision sobre venta o reposicion, disminucion o aumento de stock
            while not op_venta.isalpha():       # Verificacion de string
                op_venta = input("Error, ingrese una opcion valida. Venta o Ingreso de mercadería? (V/I): ").strip().upper()
            if op_venta == 'V':         # Si es venta

                herr_vend = input("Herramienta: ")
                while not herr_vend.isalpha():      # Verificacion de string
                    herr_vend = input("Error, ingrese una herramienta valida: ")
                herr_vend = herr_vend.strip().capitalize()
                if not herr_vend in herramientas:   # Verificacion de ausencia de herramienta en la lista del sistema
                    print("Error. La herramienta ingresada no se encuentra cargada en el sistema.")
                else:
                    cant_vend = input("Unidades a vender: ")    
                    while not cant_vend.isdigit():      # Verificacion de entero
                        cant_vend = input("Error, ingrese una cantidad valida: ")
                    cant_vend = int(cant_vend)

                    if cant_vend <= existencias[herramientas.index(herr_vend)]:     # Validacion de cantidades
                        existencias[herramientas.index(herr_vend)] -= cant_vend
                        print(f"Stock actualizado, quedan {existencias[herramientas.index(herr_vend)]} unidades de {herr_vend}")
                    else:           #Si el stock es insuficiente
                        print("Error. No hay suficientes unidades disponibles.")
                

            elif op_venta == 'I':       # Si es ingreso de mercaderia

                herr_ing = input("Herramienta: ")
                while not herr_ing.isalpha():      # Verificacion de string
                    herr_ing = input("Error, ingrese una herramienta valida: ")
                herr_ing = herr_ing.strip().capitalize()

                if herr_ing in herramientas:
                    cant_ing = input("Cantidad a sumar: ")
                    while not cant_ing.isdigit():
                        cant_ing = input("Error, ingrese una cantidad valida: ")
                    cant_ing = int(cant_ing)                
                    existencias[herramientas.index(herr_ing)] += cant_ing
                    print(f"Se han agregado {cant_ing} unidades de {herr_ing}")
                else:
                    print("La herramienta no existe en el sistema.")
            else:
                print("Error. Ingreso una opcion invalida.")
        
        case 8:         # Salir

            print("Cerrando sesion - ¡Gracias por usar el sistema!")
            fin_sist = True

        case _:         # Opcion invalida

            print("Error. Ingresa una opcion valida (1 - 8)")