#Crea un programa que:
# Pida números al usuario
# El programa termina cuando el usuario escriba 0
#Guarde todos los números en una lista
#Al final muestre:
    #todos los números ingresados
    #el número mayor

numeros = []
numero = int(input("ingrese un numero : "))

while numero != 0:
    numeros.append(numero)
    numero = int(input("ingrese un numero: "))

print("numeros ingresados: ")

for n in numeros:
    print(n)

mayor = numeros[0]

for n in numeros:
    if n > mayor:
        mayor = n

print("Numero mayor:", mayor)