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

