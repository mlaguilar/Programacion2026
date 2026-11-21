"""El mismo expediente, con Pandas y las mismas tres funciones."""
import pandas as pd
from pathlib import Path

ARCHIVO_CSV = Path(__file__).with_name("atenciones.csv")


def explorar_atenciones(atenciones):
    print('Atenciones: ', len(atenciones))
    print('Atenciones tipo: ', type(atenciones))
    print('Campos: ', list(atenciones.columns))



def contar_categorias(atenciones):
    print("Medicamentos", atenciones['medicamento'].value_counts().to_dict())
    print("Hospitales: ", atenciones['hospital'].value_counts())


def concluir(atenciones):
    print("Pacientes: ", atenciones["cedula"].nunique())
    print("Minutos espera", atenciones["minutos_espera"].sum())
    print("Promedio espera", atenciones["minutos_espera"].mean())
    print("Minutos moda", atenciones["minutos_espera"].mode())
    print("Minutos media", atenciones["minutos_espera"].median())


try:
    atenciones = pd.read_csv(ARCHIVO_CSV)
except FileNotFoundError:
    print(f"No encontramos el archivo: {ARCHIVO_CSV}")
    raise SystemExit(1)

if not atenciones.empty:
    explorar_atenciones(atenciones)
    contar_categorias(atenciones)
    concluir(atenciones)
else:
    print("El archivo no contiene atenciones.")
