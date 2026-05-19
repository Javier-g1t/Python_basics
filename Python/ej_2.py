#2)Crear un programa que ingrese el nombre de un alumno de la asignatura de floatroducción a la programación segura y calcule e imprima
#su nombre, sus notas y el promedio obtenido (20%, 35%, 35%, 10%).

#ingresamos el nombre del alumno
nombre = input("ingrese el nombre del alumno: ").strip().capitalize()

#ingresamos las notas del alumno 
n1 = float(input("ingrese la primera nota del alumno "))
n2 = float(input("ingrese la segunda nota del alumno "))
n3 = float(input("ingrese la tercera nota del alumno "))
n4 = float(input("ingrese la cuarta nota del alumno "))

#queremos calcular el promedio de las notas del alumno 
promedio = ((n1*(20/100))+(n2*(35/100))+(n3*(35/100))+(n4*(10/100)))

print(f"El promedio del alumno {nombre} es: {promedio}")
