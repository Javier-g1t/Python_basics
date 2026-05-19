#crear un programa en python que permita ingresar un numero entero y calcule e imprima si el numero ingresado es positivo o negativo o neutro

num = int(input("ingrese un N° entero: "))

if num > 0:
    print(f"{num} es positivo ")
elif num == 0:
    print(f"{num} es neutro ")
else:
    print(f"{num} es negativo ")

