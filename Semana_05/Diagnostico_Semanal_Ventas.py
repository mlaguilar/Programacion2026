"""Plantilla guiada: análisis de ventas de dos tiendas, sin ciclos."""

ventas_centro = [125000, 98000, 147000, 132000, 110000]
ventas_norte  = [140000, 135000, 150000, 145000, 155000]
meta_centro   = 640000
meta_norte    = 700000

total_centro      = sum(ventas_centro) #Total de ventas de la semana
cantidad_centro   = len(ventas_centro) #Cantidad de días registrados 
menor_centro      = min(ventas_centro) #Venta mínima del centro
mayor_centro      = max(ventas_centro) #Venta máxima del centro
promedio_centro   = total_centro/cantidad_centro
porcentaje_centro = total_centro/meta_centro * 100

total_norte      = sum(ventas_norte) #Total de ventas de la semana
cantidad_norte   = len(ventas_norte) #Cantidad de días registrados 
menor_norte      = min(ventas_norte) #Venta mínima del centro
mayor_norte      = max(ventas_norte) #Venta máxima del centro
promedio_norte   = total_norte/cantidad_norte
porcentaje_norte = total_norte/meta_norte * 100

#print(porcentaje_norte)

if total_centro > meta_centro:
    estado_centro = "meta superada"
elif total_centro == meta_centro:
    estado_centro = "meta alcanzada exactamente"
else: 
    estado_centro = "meta no alcanzada"

if total_norte > meta_norte:
    estado_norte = "meta superada"
elif total_norte == meta_norte:
    estado_norte = "meta alcanzada exactamente"
else: 
    estado_norte = "meta no alcanzada"

#print(estado_centro)

if total_centro > total_norte:
    tienda_gano = "Tienda Centro"
elif total_norte > total_centro:
    tienda_gano = "Tienda del Norte"
else:
    tienda_gano = "Ambas tiendas tiene el mismo total"

print("\t\t\tCOMPARACIÓN SEMANAL DE TIENDAS")
print("-" * 70, "\n")
print(f"Centro | total ₡{total_centro:,.2f} | meta ₡{meta_centro:,.2f} | cumplimiento {porcentaje_centro:.2f}%")
print(f"Centro logro: {estado_centro}")
print(f"Norte | total ₡{total_norte:,.2f} | meta ₡{meta_norte:,.2f} | cumplimiento {porcentaje_norte:.2f}%")
print(f"Norte logro: {estado_norte}")

