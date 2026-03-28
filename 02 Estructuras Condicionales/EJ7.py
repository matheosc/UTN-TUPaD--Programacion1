# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

vocales = ['a','e','i','o','u']

texto = input("Ingrese una frase o palabra: ")

if (texto[len(texto)-1] in vocales):
    texto = texto + "!"

print(texto)