"""
Crear un programa que permita gestionar las notas de varios estudiantes.

El programa debe:

1. Permitir ingresar estudiantes hasta que el usuario decida parar.
2. Por cada estudiante se debe ingresar:
   - Nombre
   - 3 notas (por ejemplo: prueba1, prueba2, prueba3)

3. Calcular el promedio de cada estudiante usando una función.

4. Guardar la información en una estructura como:
   (nombre, nota1, nota2, nota3, promedio)

5. Mostrar un listado completo de todos los estudiantes con sus datos.

6. Permitir buscar un estudiante por nombre y mostrar:
   - sus notas
   - su promedio
   - si está aprobado o reprobado

   (aprobado si promedio >= 4.0)

7. Mostrar:
   - el estudiante con mayor promedio
   - el estudiante con menor promedio
"""


datos= []
datos_completos = []

def ingresar():
    seguir = "si"
    while seguir == "si":
        nombre = input("ingrese el nombre del alumno: ").capitalize()
        n1 = float(input("ingrese la primera nota del alumno: "))
        n2 = float(input("ingrese la segunda nota del alumno: "))
        n3 = float(input("ingrese la tercera nota del alumno: "))
        dato = (nombre, n1,n2,n3)
        datos.append(dato)
        seguir = input("¿Desea ingresar otro alumno? (si/no): ")


def promedio(n1,n2,n3):
    return (n1+n2+n3)/3

ingresar()

for a in datos:
    nombre = a[0]
    prueba1 = a[1]
    prueba2 = a[2]
    prueba3 = a[3]
    prom = promedio(prueba1,prueba2,prueba3)
    dato_completo = (nombre, prueba1,prueba2,prueba3,prom)
    datos_completos.append(dato_completo)

def busqueda():
    encontrado = False
    alumno_buscado = input("ingrese el nombre del alumno buscado: ").capitalize
    for i in datos_completos:
        if alumno_buscado == i[0]:
            if i[4] >= 4.0:
                situacion = "APROBADO"
            else:
                situacion = "REPROBADO"
            encontrado = True
            print(f"{i[0]} sus notas son {i[1]},{i[2]},{i[3]} y su promedio es {i[4]} y su estado es {situacion:.2f}")
            break
    if not encontrado:
        print(f"{alumno_buscado}, no se encuentra registrado")


mayor = datos_completos[0]
menor = datos_completos[0]

for v in datos_completos:
    if v[4] > mayor[4]:
        mayor = v

    if v[4] < menor[4]:
        menor = v

print("\n--- RESULTADOS ---")

print(f"Mayor promedio: {mayor[0]} con {mayor[4]}")
print(f"Menor promedio: {menor[0]} con {menor[4]}")


print("---LISTA DE ALUMNOS---")
for d in datos_completos:
    print(f"{d[0]} → notas: {d[1]}, {d[2]}, {d[3]} | promedio: {d[4]}")

busqueda()