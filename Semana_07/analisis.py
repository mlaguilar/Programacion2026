from sedes import sedes

print("Sedes registradas:", len(sedes))
print("Primera sede:", sedes[0]["nombre"])
print("Ventas de la primera sede:", sedes[0]["ventas"])

print("\n Análisis semanal de emprendimientos")

for sede in sedes:
    total_ventas = sum(sede["ventas"])
    porcentaje = (total_ventas / sede["meta"]) * 100
    
    if porcentaje >= 100:
        estado ="Meta alcanzada"
    elif porcentaje >= 80:
        estado = "Cerca de la meta"
    else:
        estado = "Requiere atención"
    print(f"{sede['nombre']} | Total:₡{total_ventas:,.2f} | Meta:₡{sede['meta']:,.2f} | Porcentaje: {porcentaje:.2f}% | Estado: {estado}")