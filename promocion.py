producto = ["Cafe", 5000, 20]
porcentaje_aumento = 18

descuento = producto[1] * 15 /100
precio_promocional = producto[1] - descuento
ingreso_actual = producto[1] * producto[2]
aumento = producto[2] * porcentaje_aumento / 100
producto[2] = producto[2] + aumento
ingreso_proyectado = precio_promocional * producto[2]
diferencia = ingreso_proyectado - ingreso_actual

if diferencia > 0:
    print ("Lanzar")
else:
    print ("No lanzar")