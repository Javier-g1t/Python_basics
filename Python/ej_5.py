#crear un programa que permita ingresar el nombre y el promedio de los 40 alumnos de un curso, calcule e imprima lo siguiente :
#cantidad de alumnos que su promedio es mayor a 6 
#el promedio general del curso

cont = 1
cont_prom = 0 
ac_prom = 0
nombres = []
promedios = []

while cont <= 2: 
    nombre = input("ingrese el nombre del alumno: ").capitalize()
    nombres.append(nombre)
    promedio = float(input("ingrese la promedio del alumno: "))
    promedios.append(promedio)
    ac_prom += promedio
    if promedio > 6:
        cont_prom += 1
    cont += 1

prom_general = ac_prom/2

print(f"{'Nombre':<10} {'Promedio':<5}")
for nombre, promedio in zip (nombres, promedios):
    print(f"{nombre:<10} {promedio:<5}")
    
print(f"el promedio de alumnos con promedio mayor a 6 es igual a {cont_prom}")

print(f"el promedio general del curso es {prom_general}")






