# EJERCICIO 7

# 7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
# ● Calcular el promedio de las mínimas y el de las máximas.
# ● Mostrar en qué día se registró la mayor amplitud térmica.

temp_semanal = [[12, 27], [15, 24], [16, 23], [24, 36], [13, 25], [13, 31], [18, 22]]
amplitudes_term = []
max_amp = 0
suma_max = 0
suma_min = 0

for d in range(len(temp_semanal)):
    suma_min += temp_semanal[d][0]
    suma_max += temp_semanal[d][1]
    amplitudes_term.append(temp_semanal[d][1] - temp_semanal[d][0])

for i in range(len(amplitudes_term)):
    if amplitudes_term[i] > max_amp:
        max_amp = amplitudes_term[i]
        pos = i

print(f"El promedio de las temperaturas maximas es de: {suma_max/7:.2f}")
print(f"El promedio de las temperaturas minimas es de: {suma_min/7:.2f}")
print(f"El dia que se presento mayor amplitud termica fue el dia N.{pos+1}")