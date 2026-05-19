#crear un programa que permita ingresar un numero entero y que permita ingresar, si el numero ingresado es positivo, negativo o neutro, si el numero ingresado es par o impar, si el numero ingresado es divisble por 5, hacerlo usando la funcion definir

def entero():
    return int(input("ingrese su numero entero: "))

def num(n):
    if n > 0:
        return "positivo"
    elif n < 0:
        return "negativo"
    else:
        return "neutro"

def par_impar(n):
    if n % 2 == 0:
        return "par"
    else:
        return "impar"
    
def divisible(n):
    if n % 5 == 0:
        return "es divisible por 5"
    else:
        return "no divisible por 5"
    
def imprimir(n,tipo,pariedad,div):
    print(f"El numero {n} es {tipo}, es un numero {pariedad} y {div}")

#programa principal
n = entero()

tipo = num(n)
pariedad = par_impar(n)
div = divisible(n)

imprimir(n,tipo,pariedad,div)