#Crear un programa que:
    #Pida números al usuario
    #El programa termina cuando el usuario escriba 0
    #Al final debe mostrar:
        #cantidad de números ingresados
        #suma total

suma = 0
contador = 0

numero = int(input("ingrese un numero: "))


while numero != 0:
    suma += numero
    contador += 1
    numero = int(input("ingrese un numero: "))

print("la suma total es:", suma)
print("cantidad de numeros ingresados:", contador)
