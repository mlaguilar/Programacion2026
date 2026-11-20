"""SEMANA 09 | Práctica final: control de tiempos de espera.

Propósito: aplicar for, while, acumuladores, condicionales y una función sencilla.
Resuelva los cinco TODO. No necesita CSV, diccionarios ni try/except.

Indicaciones: para la Parte B ingrese únicamente números enteros >= 0.
Escriba 0 cuando quiera terminar el registro.
"""

# PARTE A: procesar una lista ya preparada.
ESPERAS = [12, 35, 20, 48, 15]


def sumar_esperas(lista_minutos):
    """Devuelve la suma de los tiempos (en minutos)."""
    total = 0

    for minutos in lista_minutos:
        total += minutos

    return total


print("=== PARTE A: ATENCIONES YA REGISTRADAS ===")
print("Tiempos:", ESPERAS)

total_minutos = sumar_esperas(ESPERAS)

# TODO 2: calcule el promedio usando total_minutos y len(ESPERAS).
# Sustituya el 0 por la expresión correspondiente.
promedio = total_minutos/len(ESPERAS)

esperas_largas = 0
for minutos in ESPERAS:
    if minutos > 30:
        esperas_largas += 1
    pass

print("Total de minutos:", total_minutos)
print("Promedio de minutos:", round(promedio, 2))
print("Esperas mayores a 30 minutos:", esperas_largas)


# PARTE B: registrar nuevos tiempos hasta que la persona escriba 0.
print("\n=== PARTE B: REGISTRO INTERACTIVO ===")
print("Escriba 0 para terminar. Ingrese solo números enteros no negativos.")

cantidad = 0
total_registrado = 0
respuesta = input("Minutos de espera (0 para salir): ")

while respuesta != "0":
    respuesta = int(respuesta)
    # Sustituya el 0 por la expresión correspondiente.
    total_registrado += respuesta
    cantidad += 1
    pass

    # Esta línea ya está lista; permite continuar o terminar el ciclo.
    respuesta = input("Minutos de espera (0 para salir): ")

print("Atenciones registradas:", cantidad)
print("Total de minutos registrados:", total_registrado)
