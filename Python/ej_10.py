#5.	crear un programa que permita ingresar el nombre de un alumno y sus 3 notas. El programa debe calcular e imprimir el nombre del alumno, sus 3 notas, el promedio obtenido y su situación final. aprueba si el promedio es mayor o igual a 4 y reprueba en caso contrario

nombre = input("ingrese el nombre del alumno: ")
n1 = float(input("ingrese la primera nota del alumno: "))
n2 = float(input("ingrese la tercera nota del alumno: "))
n3 = float(input("ingrese la segunda nota del alumno: "))
promedio = (n1+n2+n3)/3
if promedio > 4.0:
    fin = "APROBADO"
else:
    fin = "REPROBADO"

print(f"{nombre} sus notas son {n1}, {n2}, {n3}")
print(f"su promedio es {promedio}")
print(f"su situacion final es {fin}")