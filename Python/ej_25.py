#crear un sistema informatico que permita ingresar el nombre y el sueldo de los 30 trabajadores de una empresa. calcule e imprima lo siguiente
# cantidad de trabajadores que su sueldo es inferior a un millon de pesos}
# el total de dinero que cancela la empresa por concepto de sueldo  
#

def ingresar_datos():
    cont = 1
    for x in range(4):
        nombre = input("ingrese el nombre del trabajador: ")
        sueldo = int(input("ingrese el sueldo del trabajador: $ "))
        trabajadores[cont]=(nombre, sueldo)
        cont += 1
def recorrer():
    for c,v in trabajadores.items():
        nom, su = v
        print(f"{c}, {v} su nombre es {nom} y gana ${su}")

def sueldo_menor():
    cont = 0
    for c,v in trabajadores.item():
        nom,su = v
        if su < 100000:
            cont+= 1
    print(f"cantidad de trabajadores con sueldo menor a un 1 millon son {cont}")

def totaL_dinero():
    ac=0
    for c,v in trabajadores.items():
        nom,su = v
        ac += su
    print(f"total de dinero que cancela la empresa es ${ac}")

#PROGRAMA PRINCIPAL
trabajadores = {}
ingresar_datos()
sueldo_menor()
recorrer()
totaL_dinero()
print(trabajadores)
