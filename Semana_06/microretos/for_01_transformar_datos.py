"""Micro-reto 1: transformar datos con for.

Contexto: datos ficticios de minutos de estudio registrados en un curso
universitario de UMCA.

Prediga el resultado, complete el ciclo y compruebe su respuesta.
"""

minutos_estudio = [60, 120, 90, 85]
horas_estudio = []

for minutos in minutos_estudio:
    horas = minutos / 60
    horas_estudio.append(horas)
print("Horas de estudio:", horas_estudio)

# Resultado esperado: [1.0, 2.0, 1.5]
