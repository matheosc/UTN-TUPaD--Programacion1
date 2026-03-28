# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".

pwd = input("Ingrese una contraseña con longitud 8 a 14: ")

if (len(pwd)>7 and len(pwd)<15):
    print("Ha ingresado una contraseña correcta") 
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")