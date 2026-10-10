"""Microreto: el portero del café."""

nombre = input("Ingrese su nombre: ").upper().strip()
energia = int(input("¿Cuanta energía tiene de 0 a 100?: "))
trae_cafe = input("¿Traes cafe? (si/no): ").lower().strip() == 'si'

mensaje = ''
# Si menos 50% y no tengo cafe: descansar
# Si 50% o mas o tenga cafe: Puede ingresar a la clase
# Cualquier otro escenario: Portero confundido, revisar respuestas
if energia < 50 and not(trae_cafe):
    print("Descansar")
elif energia >= 50 or trae_cafe:
    print("Puede ingresar a la clase")
else:
    print("Portero confundido")
print(f"{nombre}: {mensaje}")