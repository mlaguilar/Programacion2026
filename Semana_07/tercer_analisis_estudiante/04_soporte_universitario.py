"""Caso 4: analice los registros de soporte sin crear funciones propias."""

from incidencias import incidencias

# Cada incidencia es un diccionario: id, provincia, categoria,
# minutos_atencion y resuelto (True o False).

# TODO: Prepare un acumulador de minutos, un diccionario para contar
#       "Acceso", "Equipo" y "Red", un contador de casos pendientes,
#       un set de provincias con pendientes, una lista de tuplas de casos
#       urgentes y una tupla para el caso con más minutos de atención.
minutos_tot = 0
casos_pendientes = 0
minutos_mayor = 0
conteos = {"Acceso":0, "Equipo":0, "Red":0}
prov_pend = set()
casos_urgentes = []
mayor_minutos = ()
# TODO: Recorra incidencias una sola vez. Actualice los acumuladores y el
#       conteo de la categoría de cada registro.
for i in range(len(incidencias)):
    minutos_tot += incidencias[i]["minutos_atencion"]
    if incidencias[i]["minutos_atencion"] > minutos_mayor:
        minutos_mayor = incidencias[i]["minutos_atencion"]
    if incidencias[i]["resuelto"] == False:
        casos_pendientes += 1
        prov_pend.add(incidencias[i]["provincia"])
        if incidencias[i]["minutos_atencion"] >= 60:
            casos_urgentes.append((incidencias[i]["id"], incidencias[i]["minutos_atencion"]))
            if incidencias[i]["minutos_atencion"] == minutos_mayor:
                mayor_minutos = (incidencias[i]["id"], minutos_mayor)
    if incidencias[i]["categoria"] == "Acceso":
        conteos["Acceso"] +=1
    elif incidencias[i]["categoria"] == "Equipo":
        conteos["Equipo"] +=1
    else:
        conteos["Red"] +=1


print(f"La cantidad de casos es {len(incidencias)}")
print(f"La cantidad de minutos en total es {minutos_tot}")
print(f"El promedio de minutos por caso es {minutos_tot/len(incidencias)}")
print(conteos)
print(f"Existen {casos_pendientes} pendientes en {len(prov_pend)} provincias")
print(f"El caso más largo es {mayor_minutos[0]} con {mayor_minutos[1]} minutos")
print("La lista de urgentes es")
print(casos_urgentes)
print("Las provincias con pendientes son")
print(prov_pend)

# Control: 10 casos; 500 minutos; promedio 50; Acceso 4, Equipo 3, Red 3;
# 4 pendientes en 4 provincias; urgentes INC-02, INC-05 e INC-07;
# más largo INC-07 con 95 minutos; hay pendientes en San Jose.
# Prueba: cambie temporalmente INC-07 a resuelto=True. Debe salir de la
# lista de urgentes, del conteo de pendientes y del set de provincias
# pendientes, pero seguir como caso más largo. Restaure incidencias.py.
