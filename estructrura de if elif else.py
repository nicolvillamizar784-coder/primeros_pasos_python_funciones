# ***** PROGRAMA PARA IDENTIFICAR SI UN NUMERO ES POSITIVO, NEGATIVO O NEUTRO *****

def capturar_datos():
    numero = int(input("Digite un número: "))
    return numero


def analizar_datos(numero):
    if numero > 0:
        resultado = "El número es Positivo."
    elif numero == 0:
        resultado = "El número es Neutro."
    else:
        resultado = "El número es Negativo."
    return resultado


def mostrar_datos(resultado):
    print("-------------------------------------")
    print("Resultado del análisis:")
    print(resultado)
    print("-------------------------------------")


# ***** CÓDIGO PRINCIPAL *****
def main():
    numero = capturar_datos()
    resultado = analizar_datos(numero)
    mostrar_datos(resultado)


# Llamado al programa principal
main()