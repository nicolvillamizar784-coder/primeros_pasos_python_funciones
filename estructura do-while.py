#*****zona funciones ******

def capturar_datos():
    print("\n-menu principal-")
    print("Digite la letra 'A' para actualizar sistema")
    print("Digite la letra 'E' para eliminar catalogo")
    print("Digite la letra 'C' para crear productos")
    print("Digite la letra 'S' pera salir del programa")
    
    letra=input("seleciona una opcion:")
    return letra.upper()

def analizar_datos(opcion):
    if opcion=="A":
        return "usted eligio actualizar sistema"
    elif opcion=="E":
        return "usted eligio eliminar catalogo"
    elif opcion=="C":
        return "usted eligio crear productos"
    elif opcion=="S":
        return "S"
    else:
        return "la informacion no es válida, intenta de nuevo."

def mostrar_datos(resultato):
    print("\n>",resultato,"\n")
    
#********** codigo principal***********

while True:
    opcion=capturar_datos()
    resultado=analizar_datos(opcion)
    
    if resultado=="S":
        print("\nFinalizo el programa con exito.\n")
        break
    
    mostrar_datos(resultado)
    
    print("el do-while a finalizado")
    
    
