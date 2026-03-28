# EJERCICIO 3

# Contexto
# Hay 2 días de atención: Lunes y Martes.
# Cada día tiene cupos fijos:
#       • Lunes: 4 turnos
#       • Martes: 3 turnos
# Reglas
#   1. Pedir nombre del operador (solo letras).
#   2. Menú repetitivo hasta salir:
#       1. Reservar turno
#       2. Cancelar turno (por nombre)
#       3. Ver agenda del día
#       4. Ver resumen general
#       5. Cerrar sistema
#   3. Reservar:
#       o Elegir día (1=Lunes, 2=Martes).
#       o Pedir nombre del paciente (solo letras).
#       o Verificar que no esté repetido en ese día (comparando con las variables ya cargadas).
#       o Guardar en el primer espacio libre (ej. lunes1, lunes2…).
#   4. Cancelar:
#       o Elegir día.
#       o Pedir nombre del paciente (solo letras).
#       o Si existe, cancelar y dejar el espacio vacío ("").
#   5. Ver agenda del día:
#       o Mostrar los turnos del día en orden (Turno 1..N), indicando “(libre)” si está vacío.
#   6. Resumen general:
#       o Turnos ocupados y disponibles por día.
#       o Día con más turnos (o empate).
# Restricciones
# • ❌ No listas, no diccionarios, no sets, no tuplas.
# • ✅ Se permite usar "" como “vacío”.
# • ✅ Validaciones con .isalpha() y .isdigit() (sin try/except)

lunes1 = ''
lunes2 = ''
lunes3 = ''
lunes4 = ''
martes1 = ''
martes2 = ''
martes3 = ''
cont_lunes = 0
cont_martes = 0
menu = True

nombre = input("Ingrese su nombre: ")

while not nombre.isalpha():
    nombre = input("Ingrese un nombre valido: ")

while menu:
    opcion = input("""1. Reservar turno
2. Cancelar turno (por nombre)
3. Ver agenda del dia
4. Ver resumen general
5. Cerrar sistema
""")
    if not opcion.isdigit():
        print("Error: ingrese un numero del 1 al 5")
    else:
        match opcion:
            case '1':
                dia = input("Elegi un dia (1.Lunes / 2.Martes): ")
                nombre = input("Ingrese su nombre: ").capitalize()
                match dia:
                    case '1':
                        if nombre != lunes1 and nombre != lunes2 and nombre != lunes3 and nombre != lunes4:
                            if lunes1 == '':
                                lunes1 = nombre
                                cont_lunes += 1
                            elif lunes2 == '':
                                lunes2 = nombre
                                cont_lunes += 1
                            elif lunes3 == '':
                                lunes3 = nombre
                                cont_lunes += 1
                            elif lunes4 == '':
                                lunes4 = nombre
                                cont_lunes += 1
                            else:
                                print("Error: los turnos del dia estan completos.")
                        else:
                            print("Error: ya tiene un turno para este dia.")
                    case '2':
                        if nombre != martes1 and nombre != martes2 and nombre != martes3:
                            if martes1 == '':
                                martes1 = nombre
                                cont_martes += 1
                            elif martes2 == '':
                                martes2 = nombre
                                cont_martes += 1
                            elif martes3 == '':
                                martes3 = nombre
                                cont_martes += 1
                            else:
                                print("Error: los turnos del dia ya estan completos.")
                        else:
                            print("Error: ya tiene un turno para este dia")
                    case _:
                        print("Error: ingresó una opción de día inválido.")
            case '2':
                dia = input("Ingrese el dia de su turno a cancelar (1.Lunes / 2.Martes): ")
                nombre = input("Ingrese su nombre: ").capitalize()
                match dia:
                    case '1':
                        if lunes1 == nombre:
                            lunes1 = ''
                            cont_lunes -= 1
                        elif lunes2 == nombre:
                            lunes2 = ''
                            cont_lunes -= 1
                        elif lunes3 == nombre:
                            lunes3 = ''
                            cont_lunes -= 1
                        elif lunes4 == nombre:
                            lunes4 = ''
                            cont_lunes -= 1
                        else:
                            print("Error: no tiene agendado ningun turno para este dia")
                    case '2':
                        if martes1 == nombre:
                            martes1 = ''
                            cont_martes -= 1
                        elif martes2 == nombre:
                            martes2 = ''
                            cont_martes -= 1
                        elif martes3 == nombre:
                            martes3 = ''
                            cont_martes -= 1
                        else:
                            print("Error: no tiene agendado ningun turno para este dia")
                    case _:
                        print("Error: ingresó una opción de día inválido.")
            case '3':
                opcion = input("Ingrese un dia para ver la agenda (1.Lunes / 2.Martes): ")
                if opcion == '1':
                    if lunes1 == '':
                        print("Lunes - Turno 1 : Libre")
                    else:
                        print(f"Lunes - Turno 1 : {lunes1}")
                    if lunes2 == '':
                        print("Lunes - Turno 2 : Libre")
                    else:
                        print(f"Lunes - Turno 2 : {lunes2}")
                    if lunes3 == '':
                        print("Lunes - Turno 3 : Libre")
                    else:
                        print(f"Lunes - Turno 3 : {lunes3}")
                    if lunes4 == '':
                        print("Lunes - Turno 4 : Libre")
                    else:
                        print(f"Lunes - Turno 4 : {lunes4}")
                elif opcion == '2':
                    if martes1 == '':
                        print("Martes - Turno 1 : Libre")
                    else:
                        print(f"Martes - Turno 1 : {martes1}")
                    if martes2 == '':
                        print("Martes - Turno 2 : Libre")
                    else:
                        print(f"Martes - Turno 2 : {martes2}")
                    if martes3 == '':
                        print("Martes - Turno 3 : Libre")
                    else:
                        print(f"Martes - Turno 3 : {martes3}")
                else:
                    print("Error: ingresó una opción de día inválido.")
            case '4':
                if lunes1 == '':
                    print("Lunes - Turno 1 : Libre")
                else:
                    print(f"Lunes - Turno 1 : {lunes1}")
                if lunes2 == '':
                    print("Lunes - Turno 2 : Libre")
                else:
                    print(f"Lunes - Turno 2 : {lunes2}")
                if lunes3 == '':
                    print("Lunes - Turno 3 : Libre")
                else:
                    print(f"Lunes - Turno 3 : {lunes3}")
                if lunes4 == '':
                    print("Lunes - Turno 4 : Libre")
                else:
                    print(f"Lunes - Turno 4 : {lunes4}")
                if martes1 == '':
                    print("Martes - Turno 1 : Libre")
                else:
                    print(f"Martes - Turno 1 : {martes1}")
                if martes2 == '':
                    print("Martes - Turno 2 : Libre")
                else:
                    print(f"Martes - Turno 2 : {martes2}")
                if martes3 == '':
                    print("Martes - Turno 3 : Libre")
                else:
                    print(f"Martes - Turno 3 : {martes3}")
                if cont_lunes > cont_martes:
                    print(f"El dia lunes tiene mas turnos ocupados ({cont_lunes})")
                elif cont_lunes < cont_martes:
                    print(f"El dia martes tiene mas turnos ocupados ({cont_martes})")
                else:
                    print(f"Ambos dias tienen la misma cantidad de turnos ocupados ({cont_lunes})")
            case '5':
                print("El sistema ha finalizado.")
                menu = False
            case _:
                print("Error: ingrese una opcion valida.")