#7.	crear un programa que permita ingresar el nombre y las 4 notas de un alumno: . Calcule e imprima: el nombre del alumno: , sus notas y el promedio obtenido. Para el cálculo del promedio considere que la primera nota equivale a un 15% del promedio, la segunda nota equivale a un 20% del promedio, la tercera nota equivale a un 35% del promedio y la cuarta nota equivale a un 30% del promedio.


def nombre():
    return input("ingrese el nombre del alumno: ")
def nota():
    puesto = ["primera","segunda","tercera","cuarta"]
    notas = []
    for i in range(4):
        nota =  float(input(f"ingrese la {puesto[i]} nota del alumno: "))
        while nota < 1 or nota > 7:
            print("---INGRESE UN VALOR VALIDO ENTRE 1 Y 7---")
            nota = float(input(f"ingrese la {puesto[i]} nota del alumno: "))
        notas.append(nota)
    return notas


def promedio(notas):
    return ((notas[0]*0.15)+(notas[1]*0.20)+(notas[2]*0.35)+(notas[3]*0.30))
    

def situacion(prom):
    if prom >= 4.0:
        return "APROBADO"
    else:
        return "REPROBADO"

def imprimir(prom,nom,estado):
    print(f"{nom} su promedio es {prom} y su situacion final es {estado}")

#PROGRAMA
nom = nombre().strip().capitalize()
notas = nota()

prom = promedio(notas)
estado = situacion(prom)

imprimir(prom,nom,estado)


