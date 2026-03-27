
#forma no optima de sumar valores 
#def suma(lista):
#   numeros_sumados = 0
#   for numero in lista:
#        numeros_sumados = numeros_sumados + numero
#    return numeros_sumados

#esultado = suma([5,3,9,10,20,3])

#forma optima de sumar valores 
def suma_total(numeros):
    return sum([*numeros])

resultado2 = suma_total([5,3,9,10,20,3])

#lo mismo de arriba pero utilizando el operador * como parametro ("args")
def suma(nombre, *numeros):
    return f"{nombre}, la suma de tus numeros es igual a : {sum(numeros)}"

resultado = suma("lucas", 4,5,6,7,9)
print(resultado)