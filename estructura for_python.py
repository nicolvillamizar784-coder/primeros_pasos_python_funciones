# Programa que suma una cantidad de números usando FOR
#_____________________________________________________

def capturar_datos():
    """Captura la cantidad de números y cada número del usuario"""
    cantidad = int(input("Digite la cantidad de números a sumar: "))
    numeros = []

    for i in range(cantidad):
        num = int(input("Digite el número " + str(i + 1) + ": "))
        numeros.append(num)
    
    return numeros


def procesar_datos(lista_numeros):
    """Procesa los números sumándolos"""
    suma = 0
    for n in lista_numeros:
        suma += n
    return suma

 
def imprimir_datos(total):
    """Imprime el resultado final"""
    print("\nLa sumatoria total es: " + str(total))


# ------------- PROGRAMA PRINCIPAL ----------------
print("=== PROGRAMA PARA SUMAR NÚMEROS (Estructura FOR) ===\n")

numeros = capturar_datos()
resultado = procesar_datos(numeros)
imprimir_datos(resultado)


