# EJERCICIO 4

# Historia
#     Sos un agente que intenta abrir una bóveda con 3 cerraduras. Tenés energía y tiempo limitados.
#     Si abrís las 3 cerraduras antes de quedarte sin energía o sin tiempo, ganás.
# Variables iniciales (NO se piden por teclado)
#         • energia = 100
#         • tiempo = 12
#         • cerraduras_abiertas = 0
#         • alarma = False
#         • codigo_parcial = ""
# Validaciones obligatorias
#         • No usar try/except.
#         • Pedir nombre del agente y validar con .isalpha() en un while.
#         • Validar opciones del menú y cualquier número pedido con .isdigit() en un while.
#         • El juego debe funcionar con estructuras secuenciales, condicionales y repetitivas (puede usar funciones propias del lenguaje como .lower(), len(), formateo, etc.).
# Regla anti-spam (muy importante)
#     Para evitar que el jugador gane eligiendo “Forzar cerradura” 3 veces seguidas al iniciar:
#         Si el jugador elige Forzar cerradura (opción 1) 3 veces seguidas, entonces:
#             • se cobra el costo normal (-20 energía, -2 tiempo), NO abre cerradura, y se activa la alarma automáticamente (alarma = True) porque “la cerradura se trabó”.
#         Si el jugador elige opción 2 o 3, se corta la racha de “forzar seguidas”.
# Menú de acciones (se repite mientras el juego siga)
#     El juego continúa mientras:
#         • energia > 0, tiempo > 0, cerraduras_abiertas < 3
#         • y no esté bloqueado por alarma.
# En cada turno mostrar el estado y el siguiente menú:
#     1. Forzar cerradura (costo: -20 energía, -2 tiempo)
#     o Si la energía está por debajo de 40, hay “riesgo de alarma”:
#     ▪ pedir un número 1-3 (validado). Si elige 3 → alarma=True.
#     o Si no hay alarma, abre 1 cerradura.
# o Regla anti-spam: si es la 3ra vez seguida forzando, se activa alarma y
# no abre.
# 2. Hackear panel (costo: -10 energía, -3 tiempo)
# o Debe usar un for de 4 pasos mostrando progreso.
# o En cada paso sumar una letra al codigo_parcial (por ejemplo “A”).
# o Si len(codigo_parcial) >= 8, se abre automáticamente 1 cerradura si
# todavía faltan.
# 3. Descansar (costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10
# energía extra)
# Regla de bloqueo por alarma
#     • Si alarma == True y tiempo <= 3 y todavía no se abrió la bóveda, el sistema se bloquea y se pierde.
# Condiciones de fin
#     • Si cerraduras_abiertas == 3 → VICTORIA
#     • Si energia <= 0 o tiempo <= 0 → DERROTA
#     • Si se bloquea por alarma → DERROTA (bloqueo)

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

            