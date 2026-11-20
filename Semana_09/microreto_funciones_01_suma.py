"""Microreto independiente: sumar tiempos con una función y un acumulador."""


ESPERAS = [12, 20, 18, 10]


def sumar_esperas(minutos):
    """Devuelve la suma de los minutos recibidos en horas."""
    total = 0

    for minuto in minutos:
        total += minuto
        

    return total/60

suma_esp = sumar_esperas(ESPERAS)

print(f"La cantidad total de tiempo de espera es {suma_esp:.2f} hora(s)")
totales = []
totales.append(sumar_esperas([20,60,20,30]))
totales.append(sumar_esperas([10,60,180,20]))
