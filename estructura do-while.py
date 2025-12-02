# Programa con estructura tipo Do-While usando tres funciones:
# capturar_datos, procesar_datos, mostrar_resultados

def capturar_datos():
    print("digite la letra 'A' para Actualizar Sistema")
    print("digite la letra 'E' para Eliminar Catalogo")
    print("digite la letra 'C' para Crear Productos")
    print("digite la letra 'S' para salir del programa")
    letra = input("Ingrese una opción: ")
    return letra   
#revisa si coloco S
#S-manda el mensaje de salida y activa (terminar)
#si no -sigue el ciclo

def procesar_datos(opcion):
    if opcion == "S" or opcion == "s":
        mensaje = "finalizo con exito \n"
        salir = True
    else:
        mensaje = "Sigue dentro del proceso\n"
        salir = False
    return mensaje, salir

def mostrar_resultados(texto):
    print(texto)

#  codigo principal 

while True:
    op = capturar_datos()

    texto, terminar = procesar_datos(op)

    mostrar_resultados(texto)

    if terminar == True:
        break

print(" finalizado \n")