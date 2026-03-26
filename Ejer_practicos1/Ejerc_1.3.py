#Crea un programa que:
#Pida el segundo números al usuario
#Guarde los números
#Al final muestre la suma total

numeros = []
suma = 0

print("--------------") 

for i in range(5):
    numero = int(input("ingrese un numero "))
    numeros.append(numero)
    suma += numero

print("--------------")

for i in range(len(numeros)):
    print("El numero", i+1, "es", numeros[i])

print("--------------")

print("la suma total de los 5 numeros da en total ", suma)

