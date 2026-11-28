"""NIVEL 3 — Seleccionar VARIAS columnas

SE PIDE
    Tome solo las columnas nombre y examen y guárdelas en la variable resultado.
    Con varias columnas el resultado vuelve a ser una tabla.

RESULTADO ESPERADO (con notas.csv)
    Una tabla con dos columnas: Valeria 92, Diego 48, Camila 72

NIVEL 3 · COMPLETAR EL HUECO. Varias columnas se piden con una LISTA, así que dentro de
notas[...] va otra lista: se ven DOS pares de corchetes, notas[["a", "b"]].
Ejecute desde la carpeta material_estudiante:  python 1_filtros_pandas/nivel_3_varias_columnas.py
"""
import pandas as pd
from pathlib import Path
ARCHIVO_CSV = Path(__file__).with_name("notas.csv")
notas = pd.read_csv(ARCHIVO_CSV)

# 1. Seleccione las columnas "nombre" y "examen" y guárdelas en la variable resultado
resultado = notas[["nombre", "examen", "proyecto"]]

# 2. Mire el resultado (esta línea ya está lista)
print(resultado.head(3))
