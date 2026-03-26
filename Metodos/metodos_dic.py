diccionario = {       #un diccionario no es una lista aunque se comporte como una
  "nombre" : "lucas",
  "apellido" : "dalto",
  "subs" : 1000000
}

#claves = diccionario[0]
#nos devuelve un objeto dict_item
claves = diccionario.keys()

#obteniendo un elemento con .get() (si no encuentra nada el programa continua)
valor_de_apellido = diccionario.get("apellido")

#eliminando un elemento del diccionario
diccionario.pop("subs")

#obteniendo un elemento dict_items iterable 
diccionario_iterable = diccionario.items()

#eliminando todo el diccionario
#diccionario.clear()

print(diccionario_iterable)