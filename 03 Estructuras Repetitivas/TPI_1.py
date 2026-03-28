# EJERCICIO 1

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

# EJERCICIO 2

cred_user = "alumno"
cred_pwd = "python123"
usuario = ""
pwd = ""
acceso = False
cont = 0
opcion = ''

while not acceso and cont < 3:
    usuario = input("Ingrese su usuario: ")
    pwd = input("Ingrese su contraseña: ")

    if usuario == cred_user and pwd == cred_pwd:
        print("Acceso concedido.")
        acceso = True
    else:
        print("Error: credenciales inválidas.")
        cont += 1

if cont == 3:
    print("Cuenta bloqueada.")

if acceso:
    print("1) Estado    2) Cambiar clave    3) Mensaje    4) Salir")
    while opcion != '4':
        opcion = input("Opción: ")
        if not opcion.isdigit():
            print("Error: ingrese un numero valido.")
        else:
            match opcion:
                case '1':
                    print("Estado: Inscripto")
                case '2':
                    nueva_pwd = input("Nueva clave: ")
                    if len(nueva_pwd) < 6:
                        print("Error: mínimo 6 caracteres.")
                    else:
                        conf_pwd = input("Ingrese nuevamente la contraseña: ")
                        if nueva_pwd == conf_pwd:
                            cred_pwd = nueva_pwd
                            print("La contraseña se ha actualizado")
                        else: 
                            print("Las contraseñas no coinciden.")
                case '3':
                    print("¡Hoy es una nueva oportunidad para brillar! Cree en ti mismo, da pequeños pasos con constancia y transforma el miedo en coraje.")
                case '4':
                    pass
                case _:
                    print("Error: opcion fuera de rango.")

# EJERCICIO 3

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

# EJERCICIO 4

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ''
forzar_cont = 0

nombre = input("Ingrese su nombre: ")
while not nombre.isalpha():
    nombre = input("Por favor ingrese un nombre valido: ")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not alarma:
    opcion = input("""1. Forzar cerradura
2. Hackear panel
3. Descansar
Opcion elegida: """)
    while not opcion.isdigit():
        opcion = input("""Por favor ingrese una opcion valida de las siguientes:
1. Forzar cerradura
2. Hackear panel
3. Descansar
""")
    match opcion:
        case '1':
            forzar_cont += 1
            energia -= 20
            tiempo -= 2
            if forzar_cont == 3:
                alarma = True
            elif energia < 40:
                num_riesgo = input("Elegi un numero del 1 al 3: ")
                while not num_riesgo.isdigit():
                    num_riesgo = input("Por favor ingresa un numero del 1 al 3")
                if num_riesgo == '3':
                    alarma = True
            if not alarma:
                cerraduras_abiertas += 1
                print(f"Has abierto una cerradura. ({cerraduras_abiertas})")
        case '2':
            forzar_cont = 0
            energia -= 10
            tiempo -= 3
            for i in range(4):
                letra = input("Ingrese una letra: ")
                codigo_parcial += letra
                print(codigo_parcial)
            if len(codigo_parcial) >= 8:
                cerraduras_abiertas += 1
        case '3':
            forzar_cont = 0
            energia += 15
            tiempo -= 1
            if energia > 100:
                energia = 100
            if alarma:
                energia -= 10
            print(f"Energia luego de descansar: {energia}")
            print(f"Tiempo luego de descansar: {tiempo}")
        case _:
            print("Error: ingresó una opcion invalida.") 

if alarma:
    print("DERROTA (BLOQUEO)")
elif energia <= 0 or tiempo <= 0:
    print("DERROTA")
elif cerraduras_abiertas == 3:
    print("VICTORIA")

# EJERCICIO 5

nombre_jugador = input("Ingrese su nombre: ")
while not nombre_jugador.isalpha():
    print("Error: Solo se permiten letras")
    nombre_jugador = input("Por favor ingrese un nombre valido: ")

vida_jugador = 100
vida_enemigo = 100
pociones = 3
ataque_pesado = 15
ataque_enemigo = 12
turno_jugador = True

print(" === INICIO DEL COMBATE === ")

while vida_enemigo > 0 and vida_jugador > 0:
    while turno_jugador:
        opcion = input(f"""Vida del jugador: {vida_jugador}
Vida del enemigo: {vida_enemigo}
Pociones restantes: {pociones}
Opciones disponibles:
1. Ataque pesado
2. Rafaga Veloz
3. Curar
Opcion elegida: """)
        while not opcion.isdigit():
            print("Error: solo se permiten numeros")
            opcion = input(f"Opcion elegida: ")
        match opcion:
            case '1':
                if vida_enemigo < 20:
                    print("Golpe critico!")
                    print(f"¡Atacaste al enemigo por {ataque_pesado*1.5} puntos de daño!")
                    vida_enemigo -= ataque_pesado * 1.5
                else: 
                    print(f"¡Atacaste al enemigo por {ataque_pesado} puntos de daño!")
                    vida_enemigo -= ataque_pesado
                turno_jugador = False
            case '2':
                for i in range(3):
                    vida_enemigo -= 5
                    print("Golpe conectado por 5 de daño")
                turno_jugador = False
            case '3':
                if pociones > 0:
                    vida_jugador += 30
                    pociones -= 1
                    print("Te has curado por 30 de vida")
                    turno_jugador = False
                else:
                    print("¡No quedan pociones!")
                    turno_jugador = False
            case _:
                print("Error: Opcion invalida, ingrese una opcion valida.")
    if vida_enemigo > 0:
        vida_jugador -= ataque_enemigo
        print("¡El enemigo te atacó por 12 puntos de daño!")
    turno_jugador = True
    if vida_enemigo > 0 and vida_jugador > 0:
        print(" ============ NUEVO TURNO ============ ")

if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre_jugador} ha ganado la batalla.")
elif vida_jugador <= 0:
    print("DERROTA. Has caído en combate.")

