#crear un programa  que permita ingresar el nombre y el promedio de notas de los 40 alumnos de un curso. calcule e imprima lo siguiente:
#cantidad de alumnos que su promedio es superior a 6.0
#promedio general del curso


def ingresar_alumnos(cantidad):
    alumnos = []

    for i in range(cantidad):
        print(f"\n--- Alumno {i+1} ---")
        
        nombre = input("Ingrese el nombre del alumno: ").strip().capitalize()

        notas = []
        for j in range(4):
            nota = float(input(f"Ingrese la nota {j+1}: "))
            while nota < 1 or nota > 7:
                print("Nota inválida (debe estar entre 1 y 7)")
                nota = float(input(f"Ingrese la nota {j+1}: "))
            notas.append(nota)

        promedio = sum(notas) / 4
        
        alumnos.append((nombre, promedio))

    return alumnos


def calcular_datos(alumnos):
    suma_promedios = 0
    mayores_6 = 0

    for __, promedio in alumnos:
        suma_promedios += promedio
        if promedio > 6:
            mayores_6 += 1

    promedio_general = suma_promedios / len(alumnos)

    return promedio_general, mayores_6


def imprimir(alumnos, promedio_general, mayores_6):
    sorted(alumnos, key=lambda x: x[1], reverse=True)
    print("\n--- RESULTADOS ---")

    for nombre, promedio in alumnos:
        print(f"{nombre}: {promedio:.2f}")

    print(f"\nEl promedio general del curso es: {promedio_general:.2f}")
    print(f"Los alumnos con promedio mayor a 6.0 son igual a: {mayores_6}")


# PROGRAMA
alumnos = ingresar_alumnos(2)  # cambia a 40 cuando quieras

prom_general, mayores_6 = calcular_datos(alumnos)

imprimir(alumnos, prom_general, mayores_6)



