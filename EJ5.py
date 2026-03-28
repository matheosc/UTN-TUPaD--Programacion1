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