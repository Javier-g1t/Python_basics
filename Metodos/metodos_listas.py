
#creando una lista con list()
lista = list([34, 56, 23, True])

#devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

#agregando un elemento a la lista, no trabajamos con una variable sino con la lista en si 
lista.append(65)

#agregando un elemento a lista en un indice en especifico
lista.insert(2, "TOMA MAMA")

#agregando varios elementos a la lista
lista.extend([False, 2030])

#elimando un elmento de la lista (por su indice)
lista.pop(3) #si queremos eliminar de atras para adelante se hace con un menos delante del numero del indice que queremos eliminar

#removiendo un elemento de la lista segun su valor
lista.remove("TOMA MAMA")

#eliminando todos los elementos de la lista 
#lista.clear()

#ORDENA la lista de forma ascendente(si usamos el parametro reverse=True lo ordena en reversa)
lista.sort(reverse=True)

#INVIERTE los elementos de una lista sin ordenar
lista.reverse()

#verificando si un elemento se encuentra en la lista
elemento_encontrado = lista.index(65)


print(dir(set(["erbfiue", "sodnhhcisnc"])))