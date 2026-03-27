# Hoy falto el profesor de clases y los chicos se organizaron para hacer su propia clase (1 sera el profesor y otro sera el asistente):
#A- pedir edad de los compañeros que vinieron hoy a clases y ordenar los datos de menor a mayor.
#B- el mayor de la clase es el profesor y el menor es el asistente: ¿quien es quien?

#funcion para obtener al asistente y al profesor segun la edad
def get_classmates(amount_classmates):

    #creando la lista con los compañeros
    classmates = []

    #ejectutando un for para pedir la informacion de cada compañero  
    for i in range(amount_classmates):
        name = input("ingrese el nombre del compañero: ")
        age = int(input("ingrese la edad del compañero: "))
        classmate = (name, age)

        #guardando la informacion en la lista
        classmates.append(classmate)

    #ordenandolos de menor a mayor segun su edad  
    classmates.sort(key=lambda x:x[1])

    #compañeros[x] devuelve una tupla con (nombre,edad) y despues accedemos al nombre 
    #para definir al asistente y al profesor 
    asisstant = classmates[0][0]
    teacher = classmates[-1][0]

    #retornamos una tupla 
    return asisstant,teacher

#desempaquetamos lo que nos retorna la funcion
asisstant,teacher = get_classmates(5)

#imprimimos el resultado
print(f"El profesor es: {teacher} y su asistente es: {asisstant}")
