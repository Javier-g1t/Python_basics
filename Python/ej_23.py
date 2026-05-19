"""
Crear un programa para una empresa que requiere calcular el sueldo semanal
de cada uno de los 100 trabajadores que trabajan en ella.

El sueldo se obtiene de la siguiente forma:

1. Si trabaja 40 horas o menos, se le paga $4000 por hora.
2. Si trabaja más de 40 horas:
   - Se le paga $4000 por cada una de las primeras 40 horas.
   - Se le paga $5500 por cada hora extra.

Las horas extras se deben calcular.

El programa debe:
- Permitir ingresar el nombre y las horas trabajadas de cada trabajador.
- Calcular su sueldo semanal.
- Mostrar un listado con los datos de cada trabajador (nombre, horas, sueldo).
- Permitir la búsqueda de un trabajador por su nombre y mostrar sus datos si existe.
"""

trabajadores = []
datos = []

def ingresar_datos():
    for i in range(3):
        nombre = input("ingrese el nombre del trabajador: ")
        horas = float(input("ingrese olas horas trabajadas: "))
        trabajador = (nombre, horas)
        trabajadores.append(trabajador)


def calcular_sueldo(horas,nombre):
        if horas <= 40:
            print(f"{nombre} trabajo 40 horas o menos ")
            sueldo = horas * 4000
        else:
            print(f"{nombre} trabajo mas de 40 hrs en la semana ")
            horas_extra = horas - 40
            sueldo = (40 * 4000) + (horas_extra * 5500)
        return sueldo


def busqueda():
    print("\n ---BUSQUEDA DE TRABAJADOR---")
    encontrado = False
    trabajador_buscado = input("Que trabajador desea buscar?: ")
    for i in datos:
        if trabajador_buscado == i[0]:
            encontrado = True
            print(f"{i[0]}, trabajo {i[1]} horas en la semana y su sueldo es de ${i[2]}")
            break
    if not encontrado:
        print(f"{trabajador_buscado} no se encuentra regristrado")

ingresar_datos()

for t in trabajadores:
    nombre = t[0]
    horas = t[1]
    sueldo = calcular_sueldo(horas,nombre)
    dato = (nombre,horas,sueldo)
    datos.append(dato)

busqueda()

for d in datos:
    print(f"{d[0]} trabajó {d[1]} horas y gana ${d[2]}")


