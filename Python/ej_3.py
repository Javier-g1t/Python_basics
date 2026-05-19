#3)Crear un programa que permita ingresar el nombre, el sueldo bruto, el porcentaje de descuento de previsión (AFP)(10%) y el porcentaje de descuento de Salud de un trabajador(7%). Imprima los datos ingresados, los montos de descuento 
#de previsión y salud y el sueldo liquido del trabajador.

nombre = (input("Ingrese el nombre del trabajador: ")).strip().capitalize()
sueldo_bruto = int(input("ingrese el sueldo bruto del trabajador: "))

dsct_afp = float(input("ingrese el porcentaje de descuento de prevision (AFP): "))
dsct_salud = float(input("ingrese el porcentaje de descuento de Salud del trabajador: "))

afp = (sueldo_bruto * dsct_afp)/100
salud = (sueldo_bruto * dsct_salud)/100

sueldo_liquido = sueldo_bruto - (afp+salud)

print(f"El sueldo liquido del/la señor/a {nombre} es igual a {sueldo_liquido}")
print(f"y los descuentoss de AFP y salud son iguales a {afp}, {salud}")


