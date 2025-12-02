# Programa que muestra el nombre del mes usando match-case

def capturar_datos():
    num = int(input("Digite un número del 1 al 12: "))
    return num


def procesar_datos(numero):
    match numero:
        case 1:
            return "Enero"
        case 2:
            return "Febrero"
        case 3:
            return "Marzo"
        case 4:
            return "Abril"
        case 5:
            return "Mayo"
        case 6:
            return "Junio"
        case 7:
            return "Julio"
        case 8:
            return "Agosto"
        case 9:
            return "Septiembre"
        case 10:
            return "Octubre"
        case 11:
            return "Noviembre"
        case 12:
            return "Diciembre"
        case _:
            return "Número inválido. Debe ser entre 1 y 12."


def imprimir_datos(resultado):
    print("\n" + resultado)


# ---------------- PROGRAMA PRINCIPAL -------------------
print("=== PROGRAMA PARA MOSTRAR EL MES SEGÚN EL NÚMERO ===\n")

numero = capturar_datos()
resultado = procesar_datos(numero)
imprimir_datos(resultado)


