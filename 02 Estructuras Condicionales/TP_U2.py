# 1_ Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. 

edad = int(input("Ingrese su edad: "))

if (edad > 18):
    print ("Es mayor de edad")

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”. 

nota = int(input("Ingrese su nota: "))

if (nota >= 6):
    print("Aprobado")
else:
    print("Desaprobado")

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par".

numero = int(input("Ingrese un numero par: "))

if (numero % 2 == 0):
    print("Ha ingresado un numero par.")
else: 
    print("Por favor, ingrese un numero par.")

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# • Niño/a: menor de 12 años.
# • Adolescente: mayor o igual que 12 años y menor que 18 años.
# • Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# • Adulto/a: mayor o igual que 30 años. 

edad = int(input("Ingrese su edad: "))

if (edad < 1):
    print("Ingrese una edad valida.")
elif (edad < 12):
    print("Niño/a")
elif (edad < 18):
    print("Adolescente/a")
elif (edad < 30):
    print("Adulto/a joven")
elif (edad >= 30):
    print("Adulto/a")

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".

pwd = input("Ingrese una contraseña con longitud 8 a 14: ")

if (len(pwd)>7 and len(pwd)<15):
    print("Ha ingresado una contraseña correcta") 
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6) Escribir un programa que solicite al usuario el consumo mensual de energía eléctrica en
# kilovatios (kWh) e indique la categoría del consumo según el siguiente criterio:
# • Menor que 150 kWh: “Consumo bajo”.
# • Entre 150 y 300 kWh (inclusive): “Consumo medio”.
# • Mayor que 300 kWh: “Consumo alto”.
# Además, si el consumo supera los 500 kWh, mostrar un mensaje adicional que diga:
# “Considere medidas de ahorro energético”.
# El programa debe imprimir por pantalla la categoría correspondiente.

consumo = int(input("Ingrese el consumo mensual en kWh: "))

if (consumo < 150):
    print("Consumo bajo")
elif (consumo <= 300):
    print("Consumo medio")
elif (consumo > 300):
    print("Consumo alto")

if (consumo > 500):
    print("Considere medidas de ahorro energético")

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

vocales = ['a','e','i','o','u']

texto = input("Ingrese una frase o palabra: ")

if (texto[len(texto)-1] in vocales):
    texto = texto + "!"

print(texto)

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:

# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.

# El programa debe transformar el nombre ingresado de acuerdo con la opción seleccionada por
# el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = input("Ingrese su nombre: ")
numero = int(input("Ingrese el numero segun la opcion que desee (1. MAYUSCULAS / 2. minusculas / 3. Capitalizadas): "))

if (numero == 1):
    print(nombre.upper())
elif (numero == 2):
    print(nombre.lower())
elif (numero == 3):
    print(nombre.title())
else:
    print("Opcion invalida, por favor ingrese un numero valido")

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# • Menor que 3: "Muy leve" (imperceptible).
# • Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# • Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# • Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# • Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# • Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud = float(input("Ingrese la magnitud de un terremoto: "))

if magnitud < 3:
    print("Muy leve")
elif magnitud < 4:
    print("Leve")
elif magnitud < 5:
    print("Moderado")
elif magnitud < 6:
    print("Fuerte")
elif magnitud < 7:
    print("Muy fuerte")
elif magnitud >= 7:
    print("Extremo")
else:
    print("Magnitud invalida, por favor ingrese una magnitud valida.")

# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año :
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

hemis = input("Ingrese en que hemisferio se encuentra (N: Norte / S: Sur): ").upper()
mes = int(input("Ingrese en que mes se encuentra (1 - 12): "))
dia = int(input("Ingrese que dia es (1 - 31): "))

if (mes < 1 or mes > 12): # Evalua si el mes es invalido
    print("Ingrese un mes valido en el rango (1-12)")

if (mes==12): # Calcula en el primer mes limite que aparece en la tabla, es decir en diciembre
    if (dia >= 21 and dia <=31):
        if (hemis == "N"):
            print("Invierno")
        elif (hemis == "S"):
            print("Verano")
        else:
            print("Formato invalido, ingrese el hemisferio correctamente.")
    elif (dia > 0 and dia < 21):
        if (hemis == "N"):
            print("Otonio")
        elif (hemis == "S"):
            print("Primavera")
        else:
            print("Formato invalido, ingrese el hemisferio correctamente.")
    else:
        print("Formato invalido, ingrese los datos correctamente.")

if (mes == 3): # Ahora le toca evaluar en marzo
    if (dia >= 21 and dia <=31):
        if (hemis == "N"):
            print("Primavera")
        elif (hemis == "S"):
            print("Otonio")
        else:
            print("Formato invalido, ingrese el hemisferio correctamente.")
    elif (dia > 0 and dia < 21):
        if (hemis == "N"):
            print("Invierno")
        elif (hemis == "S"):
            print("Verano")
        else:
            print("Formato invalido, ingrese el hemisferio correctamente.")
    else:
        print("Formato invalido, ingrese los datos correctamente.")        

if (mes == 6): # Evalua en junio
    if (dia >= 21 and dia <=30):
        if (hemis == "N"):
            print("Verano")
        elif (hemis == "S"):
            print("Invierno")
        else:
            print("Formato invalido, ingrese el hemisferio correctamente.")
    elif (dia > 0 and dia < 21):
        if (hemis == "N"):
            print("Primavera")
        elif (hemis == "S"):
            print("Otonio")
        else:
            print("Formato invalido, ingrese el hemisferio correctamente.")
    else:
        print("Formato invalido, ingrese los datos correctamente.")

if (mes == 9): # Evalua en septiembre
    if (dia >= 21 and dia <=30):
        if (hemis == "N"):
            print("Otonio")
        elif (hemis == "S"):
            print("Primavera")
        else:
            print("Formato invalido, ingrese el hemisferio correctamente.")
    elif (dia > 0 and dia < 21):
        if (hemis == "N"):
            print("Verano")
        elif (hemis == "S"):
            print("Invierno")
        else:
            print("Formato invalido, ingrese el hemisferio correctamente.")
    else:
        print("Formato invalido, ingrese los datos correctamente.")

if (mes == 1 or mes == 2): # Evalua enero y febrero
    if(hemis=="N"):
        print("Invierno")
    elif(hemis=="S"):
        print("Verano")
    else:
        print("Ingrese el hemisferio correctamente.")

if (mes == 4 or mes == 5): # Evalua abril y mayo
    if(hemis == "N"):
        print("Primavera")
    elif(hemis == "S"):
        print("Otonio")
    else:
        print("Ingrese el hemisferio correctamente.")

if (mes == 7 or mes == 8): # Evalua julio y agosto
    if (hemis == "N"):
        print("Verano")
    elif (hemis == "S"):
        print("Invierno")
    else:
        print("Ingrese el hemisferio correctamente.")

if (mes == 10 or mes == 11): # Evalua octubre y noviembre
    if (hemis == "N"):
        print("Otonio")
    elif (hemis == "S"):
        print("Primavera")
    else:
        print("Ingrese el hemisferio correctamente.")