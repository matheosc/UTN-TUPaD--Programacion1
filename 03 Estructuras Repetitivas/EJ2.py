# Requisitos
# 1. Definir credenciales fijas en el código:
#       o usuario correcto: "alumno"
#       o clave correcta: "python123"
# 2. Permitir máximo 3 intentos para ingresar usuario y clave.
# 3. Si falla 3 veces: mostrar “Cuenta bloqueada” y terminar.
# 4. Si ingresa bien: mostrar un menú repetitivo (usar while) hasta elegir salir:
#       1. Ver estado de inscripción (mostrar “Inscripto”)
#       2. Cambiar clave (pedir nueva clave y confirmación; deben coincidir)
#       3. Mostrar mensaje motivacional (1 frase)
#       4. Salir
# 5. Validación del menú:
#       o Debe ser número (.isdigit())
#       o Debe estar entre 1 y 4

# Cambio de clave
# • La nueva clave debe tener mínimo 6 caracteres (validar con len()), si no, rechazar.

# Salida esperada
# Intento 1/3 - Usuario: alumno
# Clave: xxx
# Error: credenciales inválidas.

# Intento 2/3 - Usuario: alumno
# Clave: python123
# Acceso concedido.

# 1) Estado 2) Cambiar clave 3) Mensaje 4) Salir
# Opción: a
# Error: ingrese un número válido.
# Opción: 5
# Error: opción fuera de rango.
# Opción: 2
# Nueva clave: 123
# Error: mínimo 6 caracteres.

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