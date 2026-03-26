

cadena1 = "Hola,soy,Javier"
cadena2 = "Bienvenido maquina"

#Estructura es: DATO.METODO()
#Convierte a mayusculas 
mayusc = cadena1.upper()

#Convierte a minusculas
minusc = cadena1.lower()

#primera letra en mayuscula
primer_letra_mayusc = cadena1.capitalize()

#buscamos una cadena en otra cadena, si no hay coincidencias devuelve -1
busqueda_find = cadena1.find("Hola")

#buscamos una cadena en otra cadena, si no hay coincidencias lanza error 
busqueda_index = cadena1.index("H")

#si es numerico, devolvemos true, sino devolvemos false
es_numerico_ = cadena1.isnumeric()

#si es alfanumerico devolvemos true, si no devolvemos false
es_alfanumerico = cadena1.isalpha()

#Contamos coincidencias de una cadena dentro de otra cadena; devuelve la cantidad de coincidencias
contar_coincidencia = cadena1.count("la")

#contamos cuantos caracteres tiene una cadena 
contar_caracteres = len(cadena1)

#verificamos si una cadena empieza con otra cadena ddda, si es asi devuelve true
empieza_con = cadena1.startswith("H")

#verificamos si una cadena termina con otra cadena dada, si es asi devuelve true
termina_con = cadena1.endswith("H")

#si el valor 1, se encuentra en la cadena original, reemplaza el valor 1 de la misma, por el valor 2
cadena_nueva = cadena1.replace("la", "lu")

#separar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split(",")

print(cadena_separada)

