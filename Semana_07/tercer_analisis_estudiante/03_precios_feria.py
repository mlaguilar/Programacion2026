"""Caso 3: comparación de precios de un producto en cinco ferias."""

producto = "Tomate"
precios = [900, 850, 1000, 950, 1200]
i = 0
superan = 0
promedio = sum(precios)/len(precios)
minimo = min(precios)
maximo = max(precios)
rango = maximo - minimo
while i < len(precios):
    if precios[i] > promedio:
        superan += 1
    else:
        superan += 0
    i += 1
# TODO: Clasifique el rango: >=300 variación alta; >=150 moderada; si no, baja.
if rango >= 300:
    var = "Variación alta"
elif rango >= 150:
    var = "Variación moderada"
else:
    var = "Variación baja"
print(f"El producto es {producto}")
print(f"El promedio es: ₡{promedio}")
print(f"El minimo es: ₡{minimo}")
print(f"El máximo es: ₡{maximo}")
print(f"El rango es: ₡{rango}")
print(f"{superan} precios sobre el promedio")
print(f"{var}")
