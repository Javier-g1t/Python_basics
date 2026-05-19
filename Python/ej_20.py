#crear un programa que permita ingresar 1000 numeros enteros en una lista. posteriormente calcule e imprima lo siguiente:
#cantidad de numeros negativos ingresados
#promedio de los numeros pares ingresados 


lista_de_numeros = []
contador_neg = 0
ac_pares = 0
cont_pares = 0 

for i in range(4):
    numero = int(input("ingrese un numero entero: "))
    lista_de_numeros.append(numero)
    if numero < 0:
        contador_neg +=1

for i in lista_de_numeros:
    if i % 2 == 0:
        ac_pares += i
        cont_pares += 1
if cont_pares != 0:
    prom_pares = ac_pares/cont_pares
    print(f"promedio de n° pares es {prom_pares}")
else: 
    print("no se ingresaron pares ")

print(f"se ingresaron {len(lista_de_numeros)} numeros, hay {contador_neg} numeros negativos en la lista y el promedio de numeros pares es igual {prom_pares}")