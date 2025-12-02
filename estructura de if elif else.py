# zona de funciones 

def capturar_datos():
    print("Digite un número:")
    numero = int(input())
    return numero

def procesar_datos(num):
    if num > 0:
        resultado = "El número es Positivo."
    elif num == 0:
        resultado = "El número es Neutro."
    else:
        resultado = "El número es Negativo."
    return resultado

def mostrar_resultados(texto):
    print(texto)


# ******* CÓDIGO PRINCIPAL *******

numero_ingresado = capturar_datos()
respuesta = procesar_datos(numero_ingresado)
mostrar_resultados(respuesta)