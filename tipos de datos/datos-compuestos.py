
#en python se cuenta desde el numero 0 al 9, entonces si nos queremos referir al primer obejto o string de algo debemos poner 0 en vez de uno, Javier Ramirez = elemento 1, en el indice 0, queremos el indice
#creando una lista se puede modificar 
lista = ["Javier Ramírez", "noissette", True , 1.72]
#la tupla es igual que la lista pero esta NO se puede MODIFICAR
tupla = ("Javier Ramírez", "noissette", True , 1.72)

#esto es valido 
lista[3] = "Maquinola"

#esto no es valido 
#tupla[3] = "Maquinola"

#creando un conjunto (set), no hay orden fijo, se puede modificar pero no los elementos
conjunto = {"Javier Ramírez", "noissete", True,1.72}
#conjunto[1] = "pedrin" (esto tira error porque modificamos un elemento)
#conjunto = {"ahora si funciona por que modificamos el conjunto en si"}
#a diferencia de las listas y las tuplas en los conjuntos uno no puede acceder al indice de los elementos por ejmplo, en un conjunto NO SE PUEDEN MOSTRAR DATOS DUPLICADOS
#printo(conjunto[1]), ese print tiraria error ya que no podemos acceder al indice, sin un bucle.

#creando un diccionario (dict), (la estructura es key : value y separamos con comas)
diccionario = {
    'nombre' : "Javier Ramírez",
    'canal' : "noissette",
    'esta_emocioando' : True,
    'altura' : 1.72,
    'dato_duplicado' : "noissette",
}


print(diccionario["altura"] + 2)
print(lista[3])


