#crear un programa que permita ingresar el nombre y las 3 notas de los 20 alumnos de un curso y calcule e imprima lo siguiente:
#los datos ingresados,
#el promedio y la situacion de cada alumno. si el promedio es mayor o igual a 4 la situacion es aprobado en caso contrario la situacion es reprobado
#cantidad de alumnos que su promedio sea superior a un 6
#el promedio general del curso

curso = []
promedio = []

for x in range(1):
    nombre = input("ingrese el nombre del alumno: ")
    n1 = float(input(f"ingrese la primera nota del alumno: "))
    n2 = float(input(f"ingrese la segunda nota del alumno: "))
    n3 = float(input(f"ingrese la tercera nota del alumno: "))
    alumno = (nombre,n1,n2,n3)
    curso.append(alumno)

for i in curso:
    #nom,nota1,nota2,nota3=i
    promedio = ((i[1]+i[2]+i[3])/3)
    if promedio >= 4:
        situacion = "aprobado"
    else:
        "reprobado"
    print(f"{i[0]}, sus notas fueron {i[1],i[2],i[3]} obtuvo un promedio de {promedio} y su situacion actual es {situacion}")

cont_mayor_6 = 0
for i in curso:
    promedio = ((i[1]+i[2]+i[3])/3)
    if promedio > 6:
        cont_mayor_6 +=1
print(f"cantidad de alumnos con promedio mayor a 6 son {cont_mayor_6} alumnos")

ac = 0
for i in curso:
    promedio = ((i[1]+i[2]+i[3])/3)
    ac += promedio
promedio_curso = ac/len(curso)
print(f"el promedio general del curso es {promedio_curso}")
print(curso)