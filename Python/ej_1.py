#1)Crear un programa que permita ingresar dos números enteros y calcule e imprima el resultado de las 
#operaciones aritméticas de los números ingresados.


opcion = input("ingrese la operacion que desea realizar ").lower()

num1 = int(input("ingrese su primer numero entero "))
num2 = int(input("ingrese su segundo numero entero "))

if opcion == "suma":
    suma = num1+num2  
    print(suma)
elif opcion == "resta":
    resta = num1-num2
    print(resta)
elif opcion == "division":
    while num2 == 0:
        print("ERROR")
        num2 = int(input("ingrese nuevamente su segundo numero diferente de 0 "))
    if num2 != 0:
        division = num1//num2
        print(division)
elif opcion == "multiplicacion":
    multiplicacion = num1*num2
    print(multiplicacion)
else: 
    print("operacion no valida")



