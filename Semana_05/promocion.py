producto = ["Cafe", 5000, 20]
porcentaje_aumento = 20

descuento = producto[1] * 15 /100
precio_promocional = producto[1] - descuento
ingreso_actual = producto[1] * producto[2]
aumento = producto[2] * porcentaje_aumento / 100
producto[2] = producto[2] + aumento
ingreso_proyectado = precio_promocional * producto[2]
diferencia = ingreso_proyectado - ingreso_actual





print("ANÁLISIS DE PROMOCIÓN")
print("-"*50)
print(f"Producto: {producto[0]}", "\n")
print(f"Precio actual: €{producto[1]} ", "\n")
print(f"Unidades actuales: {producto[2] - aumento}", "\n")
print(f"Ingreso actual: €{ingreso_actual}", "\n")
print(f"Descuento: €{descuento}", "\n")
print(f"Precio promocional: €{precio_promocional}", "\n")
print(f"Aumento esperado en ventas: {porcentaje_aumento}%", "\n")
print(f"Unidades proyectadas: {producto[2]}", "\n")
print(f"Ingreso con promoción: {ingreso_proyectado}", "\n")
print(f"Diferencia: {diferencia}", "\n")


if diferencia > 0:
    print ("RECOMENDACION: Lanzar")
else:
    print ("No lanzar")