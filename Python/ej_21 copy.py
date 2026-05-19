#crear un programa que permita ingresar el nombre y las 3 notas de los 20 alumnos de un curso y calcule e imprima lo siguiente:
#los datos ingresados,
#el promedio y la situacion de cada alumno. si el promedio es mayor o igual a 4 la situacion es aprobado en caso contrario la situacion es reprobado
#cantidad de alumnos que su promedio sea superior a un 6
#el promedio general del curso


def ingresar():
    for i in range(2):
        nombre = input("ingrese el nombre del alumno: ") 
        n1 = float(input("ingrese la primera nota: "))
        n2 = float(input("ingrese la primera nota: "))
        n3 = float(input("ingrese la primera nota: "))
        alumno = (nombre,n1,n2,n3)
        curso.append(alumno)

def calcular_promedio(a,b,c):
    prom = (a+b+c)/3
    return prom

def calcular_situacion(p):
    if p >= 4:
        situacion = "aprobado"
    else:
        situacion = "reprobado"
    return situacion

def listado_curso():
    for i in curso:
        promedio = calcular_promedio(i[1],i[2],i[3])
        situacion_alumno = calcular_situacion(promedio)
        print(f"{i[0]}, sus notas fueron, {i[1],i[2],i[3]}, obtuvo un promedio de, {promedio:.2f} y esta {situacion_alumno}")

def contar_promedio_mayor_6():
    cont = 0
    for i in curso:
        promedio = calcular_promedio(i[1],i[2],i[3])
        if promedio > 6:
            cont += 1
    return cont

def promedio_curso():
    ac=0
    for i in curso:
        promedio = calcular_promedio(i[1],i[2],i[3])
        ac += promedio
    prom_curso = ac/len(curso)
    return prom_curso

def imprimir():
    print(f"la cantidad de alumnos con promedio mayor a 6 fue de, {cantidad_mayor_6}")
    print(f"el promedio del curso es igual a: {promedio_general:.1f}")

#PROGRAMA PRINCIPAL
curso=[]
ingresar()
listado_curso()
cantidad_mayor_6 = contar_promedio_mayor_6()
promedio_general = promedio_curso()
imprimir()


