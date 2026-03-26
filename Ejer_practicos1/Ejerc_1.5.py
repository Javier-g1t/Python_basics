#Objetivo: filtrar numeros (for, if, lista, .append())
#Crea un programa que:

#Pida 5 números
#Guarde los números en una lista
#Al final imprima solo los números mayores que 10

numero = [] #creamos una lista vacia donde agregaremos los numeros ingresados por el usuario, esto lo haremos con .append()

#le damos al usario un rango de numeros que debe ingresar
for i in range(5): 
    #creamos una variable donde se guardaran los numeros ingresados por el usario
    n = int(input("ingrese 5 numeros ")) 
    #este es el .append() que usaremos para no perder los datos ingresados
    numero.append(n)

print("numeros mayores a 10: ")

#ahora tenemos la variable n que es igual a los numeros ingresados, y queremos revisar estos en la lista numero.
for n in numero:
    #usamos el if para seleccionar y printear solo los numeros mayores a 10 
    if n > 10:
        print(n)
