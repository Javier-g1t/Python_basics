#crear un programa que permita ingresar 1000 numeros enteros y calcule e imprima lo siguiente: 
#cantidad de numeros negativos
#promedio numeros pares 
#promedio de los numeros ingresados

def ingresar():
    numero = int(input("ingrese un numero entero: "))
    return numero

def contar_negativos():
    global cont_neg
    if numero_ingresado < 0:
        cont_neg += 1 

def acumular_contar_pares():
    global ac_pares
    global cont_pares
    if numero_ingresado%2 == 0:
        ac_pares += numero_ingresado
        cont_pares += 1

def promedio_pares():
    if cont_pares != 0:
        promedio = ac_pares/cont_pares
        return promedio
    else:
        return "0 no hay numeros pares "

def acumular_contar_ing():
    global ac_ing
    global cont_ing
    ac_ing += numero_ingresado
    cont_ing += 1

def promedio_ingresados():
    promedio = ac_ing/cont_ing
    return promedio

def imprimir(prom_pares,prom_ing):
    print("-----------------------------------------")
    print(f"Cantidad de numeros negativos ingresados es igual a {cont_neg}") 
    print("-----------------------------------------")
    print(f"El promedio de numeros pares es de {prom_pares}")
    print("-----------------------------------------")
    print(f"El promedio de los numeros totales ingresados es de {prom_ing}")
#PROGRAMA PRINCIPAL
ac_ing = 0
cont_ing = 0
ac_pares = 0 
cont_pares = 0
cont_neg = 0
for x in range(5):
    numero_ingresado = ingresar()
    contar_negativos()
    acumular_contar_pares()
    acumular_contar_ing()
prom_pares = promedio_pares()
prom_ing = promedio_ingresados()
imprimir(prom_pares,prom_ing)