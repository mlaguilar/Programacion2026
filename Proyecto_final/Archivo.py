import csv

datos = [
    ["Nombre", "Edad", "Ciudad"],
    ["Ana", 25, "San José"],
    ["Luis", 30, "Heredia"],
    ["Carlos", 28, "Cartago"]
]

with open("personas.csv", mode="w", newline="", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerows(datos)
