# EJERCICIO 7

def operaciones_basicas(a, b)-> tuple:
    return (a+b, a-b, a*b, a/b)

num_a = int(input("Ingrese un numero: "))
num_b = int(input("Ingrese otro numero: "))

suma, resta, mult, divi = operaciones_basicas(num_a, num_b)

print(f"""
Sumados = {suma}
Restados = {resta}
Multiplicados = {mult}
Divididos = {divi}
""")
