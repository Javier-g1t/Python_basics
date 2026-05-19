#4.	Crear un programa que permita ingresar el nombre y el año de nacimiento de una persona y calcule e imprima el nombre y la edad de la persona actualmente, y si corresponde a una persona mayor de edad o no. con funciones


def nombre():
    return input("Ingrese su nombre: ")
def nacimiento():
    return int(input("Ingrese su año de nacimiento: "))


def edad(nac):
    return 2026 - nac

def edad_mayor(e):
    if e >= 18:
        return "mayor de edad"
    else:
        return "menor de edad"

def imprimir(nom, e, em):
    print(f"{nom}, su edad es {e} y usted es {em}")

#PROGRAMA PRINCIPAL
nom = nombre()
nac = nacimiento()

e = edad(nac)
em = edad_mayor(e)

imprimir(nom, e, em)