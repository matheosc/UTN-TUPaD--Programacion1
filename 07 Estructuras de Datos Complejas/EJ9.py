# EJERCICIO 9

agenda = {
    ("lunes", "10:00"): "Reunion",
    ("martes", "15:00"): "Clase de Ingles"
}

dia = input("Ingrese que dia desea consultar: ").lower()
hora = input("Ingrese que hora desea consultar: ")

tup_busqueda = (dia, hora)

if tup_busqueda in agenda.keys():
    print(f"Tienes agendado la siguiente actividad: {agenda[tup_busqueda]}")
else:
    print("No tienes nada agendado para ese momento.")
