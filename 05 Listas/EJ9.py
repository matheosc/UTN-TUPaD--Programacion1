# EJERCICIO 9

# 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# ● Inicializarlo con guiones "-" representando casillas vacías.
# ● Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# ● Mostrar el tablero después de cada jugada.

tablero = [['-','-','-'],['-','-','-'],['-','-','-']]
juego_activo = True
seguir = ""
turno_uno = True
pos_c_uno = 0
pos_f_uno = 0
pos_c_dos = 0
pos_f_dos = 0

print("""            Columnas
              1 2 3
            1|-|-|-|
     Filas  2|-|-|-|
            3|-|-|-|""")

while juego_activo:

    while turno_uno:                                            # Mientras que el primer jugador no termine su turno, el segundo no podra interactuar
        print("========================================")
        print("Jugador 1: Representa una X")   

        pos_c_uno = input("Por favor ingrese la columna a marcar (1 - 3): ").strip()        
        while not pos_c_uno in ['1', '2', '3']:                 # Verificacion de la columna ingresada por el jugador uno
            pos_c_uno = input("Error, por favor ingrese un numero valido (1 - 3): ") 
        pos_c_uno = int(pos_c_uno)              

        pos_f_uno = input("Por favor ingrese la fila a marcar (1 - 3): ").strip()
        while not pos_f_uno in ['1', '2', '3']:                 # Verificacion de la fila ingresada por el jugador uno
            pos_f_uno = input("Error, por favor ingrese un numero valido (1 - 3): ") 
        pos_f_uno = int(pos_f_uno)

        match tablero[pos_f_uno-1][pos_c_uno-1]:
            case '-':                                           # Si la celda ingresada por el jugador uno esta vacia entonces
                tablero[pos_f_uno-1][pos_c_uno-1] = 'X'         # Se marca con una X
                print("Marca registrada, el tablero queda de la siguiente manera: ")
                turno_uno = False
            case 'X':                                           # Si la celda esta marcada por el jugador uno entonces
                print("Error, el jugador habia marcado esta celda anteriormente.")
            case 'O':                                           # Si la celda esta marcada por el jugador dos entonces
                print("Error, el contrincante habia marcado esta celda anteriormente.")

    print("""            Columnas
              1 2 3""")
    for f in range(3):                                      # Se imprime toda la matriz segun los contenidos
        if f != 1:
            print(f"            {f+1}|", end="")
        else:
            print(f"     Filas  {f+1}|", end="")
        for c in range(3):
            if tablero[f][c] == 'X':
                print("X", end="|")
            elif tablero[f][c] == 'O':
                print("O", end="|")
            else:
                print("-", end="|")
        print("")

    while not turno_uno:                                        # Mientras que el segundo jugador no termine su turno, el primero no podra interactuar
        print("========================================")
        print("Jugador 2: Representa una O")
        pos_c_dos = input("Por favor ingrese la columna a marcar (1 - 3): ").strip()        
        while not pos_c_dos in ['1', '2', '3']:                 # Verificacion de la columna ingresada por el jugador dos
            pos_c_dos = input("Error, por favor ingrese un numero valido (1 - 3): ") 
        pos_c_dos = int(pos_c_dos)              

        pos_f_dos = input("Por favor ingrese la fila a marcar (1 - 3): ").strip()
        while not pos_f_dos in ['1', '2', '3']:                 # Verificacion de la fila ingresada por el jugador dos
            pos_f_dos = input("Error, por favor ingrese un numero valido (1 - 3): ") 
        pos_f_dos = int(pos_f_dos)
        match tablero[pos_f_dos-1][pos_c_dos-1]:
            case '-':                                           # Si la celda ingresada por el jugador dos esta vacia entonces
                tablero[pos_f_dos-1][pos_c_dos-1] = 'O'         # Se marca con una O
                print("Marca registrada, el tablero queda de la siguiente manera: ")
                turno_uno = True
            case 'O':                                           # Si la celda esta marcada por el jugador dos entonces
                print("Error, el jugador habia marcado esta celda anteriormente.")
            case 'X':                                           # Si la celda esta marcada por el jugador uno entonces
                print("Error, el contrincante habia marcado esta celda anteriormente.")

    print("""            Columnas
              1 2 3""")
    for f in range(3):                                      # Se imprime toda la matriz nuevamente, segun los contenidos
        if f != 1:
            print(f"            {f+1}|", end="")
        else:
            print(f"     Filas  {f+1}|", end="")
        for c in range(3):
            if tablero[f][c] == 'X':
                print("X", end="|")
            elif tablero[f][c] == 'O':
                print("O", end="|")
            else:
                print("-", end="|")
        print("")

    seguir = input("Desea seguir jugando? (S/N): ").strip().upper()
    if seguir == 'N':
        juego_activo = False
        print("Gracias por haber jugado!")
    elif seguir != 'S':
        print("Caracter ingresado invalido. Por favor ingrese un caracter valido (S/N): ")
    else:
        print("Siguiente turno!")

        
