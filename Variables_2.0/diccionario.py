#creando diccionarios con dict()
diccionario = dict(nombre="lucas",apellido="dalto")

#las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["dalto", "rancio"]): "jajaja"}

#creando diccionarios con fromkeys(), valor por defecto: none 
diccionario = dict.fromkeys(["ABCD","algun valor fijo"])

#creando diccionarios con fromkeys () cambiando el valor por defecto a "no se"
diccionario = dict.fromkeys(["nombre","apellido"],"nose")

print(diccionario)