"""Semana 8: informe de atenciones hospitalarias ficticias.

Complete las fases con el docente. La lectura de datos ya está preparada.
"""

# FASE 0: CONSUMIR LA CONEXIÓN PREPARADA
# conexion_api.py se encuentra junto a este archivo.
from conexion_api import cargar_datos

registros = cargar_datos()
print("Fuente: JSON público de GitHub")
print("Atenciones recibidas:", len(registros))

# La muestra solicitada usa range(3): deben existir las posiciones 0, 1 y 2.
if len(registros) < 3:
    raise SystemExit("Se necesitan al menos 3 registros. Publique la etapa 3.")


# FASE 1: MOSTRAR Y CONTAR LOS MEDICAMENTOS DE TRES ATENCIONES
#Cada clave es un nombre de medicamento y su valor es el nombre estandarizado
equivalencias = {
    "acetaminofen" : "acetaminofén",
    "paracetamol" : "acetaminofén",
    "antiacido" : "antiácido",
    "losartán" : "losartan"
}
conteo_medicamentos = {}
total_medicamentos = 0
print("\ANALISIS FASE #1 Muestra 3")
for indice in range(3):
    registro = registros[indice]
    print(f"El paciente {registro["paciente_nombre"]}, con cedula {registro["paciente_cedula"]}, fue diagnosticado con {registro["diagnostico"]}") 
    print(f"Los medicamentos recetados son {registro["medicamentos"][0]} y {registro["medicamentos"][1]}")
    
    for medicamento in registro["medicamentos"]:
        medicamento = medicamento.strip().lower()
        if medicamento in equivalencias:
            medicamento = equivalencias[medicamento]
        total_medicamentos += 1
        if medicamento in conteo_medicamentos:
            conteo_medicamentos[medicamento] += 1
        else:
            conteo_medicamentos[medicamento] = 1

print("\nTotal de medicamentos recetados", total_medicamentos)
print(conteo_medicamentos)
# FASE 2: CONTAR LOS MEDICAMENTOS DE TODAS LAS ATENCIONES
conteo_medicamentos = {}
total_medicamentos = 0
conteo_hospital = {}
total_pacientes = 0
print("\ANALISIS FASE #2 MEDICAMENTOS Y ATENCIONES")
for registro in registros:
    total_pacientes += 1
    hospital = registro["hospital"]
    if hospital not in conteo_hospital:
        conteo_hospital[hospital]= 0
    conteo_hospital[hospital] += 1
    for medicamento in registro["medicamentos"]:
        medicamento = medicamento.strip().lower()
        if medicamento in equivalencias:
            medicamento = equivalencias[medicamento]
        total_medicamentos += 1
        if medicamento in conteo_medicamentos:
            conteo_medicamentos[medicamento] += 1
        else:
            conteo_medicamentos[medicamento] = 1
print("\nTotal de medicamentos recetados", total_medicamentos)

for medicamento, cantidad in conteo_medicamentos.items():
    print(f"- {medicamento}: \t {cantidad}")
for hospital, cantidad in conteo_hospital.items():
    print(f"- {hospital}: \t {cantidad}")
# FASE 3: CONTAR ATENCIONES POR HOSPITAL



# FASE 4: CONTAR ATENCIONES POR ENFERMEDAD DIAGNOSTICADA

