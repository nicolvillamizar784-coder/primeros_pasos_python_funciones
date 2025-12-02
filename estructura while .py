#zona de funciones 

#pide numero 
def capturar_datos():
    print("Digite un número (0 para salir): ")
    numero = int(input())
    return numero

#mientras no sea 0, revisa si es par o impar 
def procesar_datos(num):
    if num % 2 == 0:
        resultado = "El número es par"
    else:
        resultado = "El número es impar"
    return resultado

#muestra el resultado
def mostrar_resultados(texto):
    print(texto)


#Código principal 
num = 1

while num != 0:
    num = capturar_datos()

    if num != 0:
        mensaje = procesar_datos(num)
        mostrar_resultados(mensaje)

print("Finalizó el programa")