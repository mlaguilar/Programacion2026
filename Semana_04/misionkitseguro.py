#Solución: Misión Kit Seguro

nombre       = input("Nombre: ").upper().strip()
kit          = input("Tipo de kit: ").lower().strip()
autorizacion = input("¿Tiene autorización? (si/no): ").lower().strip() == 'si'

try: 
    cantidad = int(input("Número de kits: "))
except ValueError:
    print("Cantidad de kits inválida, digite del 1 al 100")
    cantidad = -1

try: 
    dias = int(input("Dias de prestamo: "))
except ValueError:
    print("Cantidad de días inválida, ingrese un número entero positivo: ")
    dias = -1

if not nombre or not kit or cantidad < 1 or dias < 1:
    resultado = "Registro rechazado: revise los datos ingresados"
elif autorizacion and cantidad <= 3 and dias <= 7:
    resultado = f"Registro aprobado para {nombre}: {cantidad} kit(s) de {kit}"
else:
    resultado = "Solicitud enviada a revisión"
print( "-" * 50, '\n')
print(resultado)
