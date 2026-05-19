#crear un programa que permita ingresar N numeros enteros y calcule e imprima lo siguiente:
# cantidad de numeros pares ingresados 
# el promedio de los numeros negativos ingresados

respuesta = "si"
cont_par = 0
ac_neg = 0
cont_neg = 0

while respuesta == "si":
    numero_ingresado = int(input("ingrese un numero entero "))
    if numero_ingresado %2 == 0:
        cont_par +=1
    if numero_ingresado < 0:
        ac_neg += numero_ingresado
        cont_neg +=1
    respuesta = input("continuar ingresando si o no : ")

print(f"cantidad de pares {cont_par}")

if cont_neg != 0:
    prom_negativos = ac_neg/cont_neg
    print(f"el promedio de negativos es {prom_negativos}")
else:
    print("no hay negativos ingresados ")

