def ingresar(mensaje):
    valor_ingresado = input(mensaje)
    return valor_ingresado

#programa principal
nombre = ingresar("ingrese su nombre : ")
apellido = ingresar("ingrese su apellid : ")

def imprimir():
    print(f"su nombre completo es {nombre} {apellido}")

imprimir()