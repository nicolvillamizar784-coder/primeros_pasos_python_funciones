   # programa para determinar si un  numero es par o impar 
   #______________________________________________________
def capturar_datos():
    """Captura un número desde consola"""
    num = int(input("Digite un número (0 para salir): "))
    return num

def procesar_datos(numero):
    """Procesa el número y determina si es par o impar"""
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

def imprimir_datos(numero, resultado):
    """Imprime el resultado del procesamiento"""
    print(f"El número {numero} es {resultado}\n")

# ---------- Programa Principal ----------
print("=== PROGRAMA PARA SABER SI UN NÚMERO ES PAR O IMPAR ===\n")

num = 1  # variable de control

while num != 0:
    num = capturar_datos()

    if num == 0:
        print("\nFinalizó el programa.")
        break

    resultado = procesar_datos(num)
    imprimir_datos(num, resultado)




