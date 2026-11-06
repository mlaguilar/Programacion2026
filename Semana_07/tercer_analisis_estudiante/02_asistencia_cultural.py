"""Caso 2: asistencia por bloques. Complete el análisis con un ciclo for."""

asistencias = [120, 180, 210, 250, 230]
capacidad = 300
total = 0
porcentaje = 0
bloques = 0

for asis in asistencias:
    total += asis
    porcentaje = asis / capacidad
    if porcentaje > 0.7:
        bloques +=1
    else:
        bloques += 0

promedio = sum(asistencias)/len(asistencias)
porcentaje_ocup = promedio/300 *100
if porcentaje_ocup >= 80:
    ocupacion = "alta"
elif porcentaje_ocup >= 50:
    ocupacion = "media"
else:
    ocupacion = "baja"

print(f"El total de asistencias es: {total}")
print(f"El promedio es: {promedio}")
print(f"La ocupación de ese promedio es: {porcentaje_ocup} %")
print(f"La cantidad de bloques que superan 70% es: {bloques}")
print(f"La ocupación en general fue: {ocupacion}")