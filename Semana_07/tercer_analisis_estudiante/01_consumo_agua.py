"""Caso 1: cambio del consumo diario de agua. Complete el programa."""

consumos_litros = [120, 115, 108, 102, 96]

consumo_total = sum(consumos_litros)
promedio_diario = consumo_total / len(consumos_litros)
litros_ahorrados = consumos_litros[0] - consumos_litros[-1]
porcentaje_reduccion = (litros_ahorrados / consumos_litros[0]) * 100
if porcentaje_reduccion >= 15:
    clasificacion = "reducción alta"
elif porcentaje_reduccion > 0:
    clasificacion = "reducción moderada"
else:
    clasificacion = "sin reducción" 
print(f"Consumo total: {consumo_total} L ")
print(f"Promedio diario: {promedio_diario} L")
print(f"Ahorro: {litros_ahorrados} L")
print(f"Reduccion: {porcentaje_reduccion} %")
print(f"Es {clasificacion}")
# Prueba: use temporalmente cinco consumos iguales. Debe indicar 0 % y
# "Sin reducción". Restaure la lista antes de entregar.
