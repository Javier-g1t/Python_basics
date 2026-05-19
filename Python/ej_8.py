#4.	Crear un programa que permita ingresar el nombre y el año de nacimiento de una persona y calcule e imprima el nombre y la edad de la persona actualmente, y si corresponde a una persona mayor de edad o no.

nombre = input("ingrese su nombre : ")
nacimiento = int(input("ingrese su año de nacimiento : "))
edad = 2026 - nacimiento

print(f"su nombre es {nombre} y su edad es {edad}")

if edad > 18:
    print("usted es mayor de edad ")
else:
    print("usted es menor de edad ")