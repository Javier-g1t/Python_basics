
animales = ["gato", "perro", "loro", "cocodrilo"]
numeros = [10,62,12,72]

#recorriendo la lista animales 
for animal in animales:
    print(f"ahora la variable animal es igual a: {animal}")

#recorriendo la lista numeros y multiplicando cada valor *10
for numero in numeros:
    resultado = numero * 10
    print(resultado)

#iterando dos listas del mismo tamaño al mismo tiempo
for numero, animal in zip(animales, numeros):
    print(f"recorriendo lista 1: {numero}")
    print(f"recorriendo lista 2: {animal}")

#forma no optima de recorrer una lista (NO FUNCIONA EN CONJUNTOS)
for num in range(len(numeros)):
    print(numeros[num])

#forma correcta de recorrer una lista con su indice 
for num in enumerate(numeros):
    #print(type(num)) esto es una tupla
    indice = num[0]
    valor = num[1]
    print(f"el indice es: {indice} y el valor es: {valor}")

#usando el for else
for numero in numeros:
    print(f"ejecuntando el ultimo bucle, valor actual: {numero}")
else:
    print("el bucle termino")


#todo lo anterior funciona exactamente igual con tuplas y conjuntos
