#pide el número del mes al usuario
def capturar_datos():
    print("Digite un número del 1 al 12:")
    numero = int(input())
    return numero


# recibe el número y devuelve el nombre del mes
def procesar_datos(num_mes):
    match num_mes:
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
            return "Número fuera de rango"


#  muestra el resultado en pantalla
def mostrar_resultados(mensaje):
    print("El mes correspondiente es:", mensaje)


# Programa principal
numero_mes = capturar_datos()
nombre_mes = procesar_datos(numero_mes)
mostrar_resultados(nombre_mes)