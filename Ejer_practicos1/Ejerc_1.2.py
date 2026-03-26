
#crear un programa que.
#1-pida al usario un numero
#muestre la tabla de multiplicar de ese numero del 1 al 10, (input, for, print)
numero = int(input("ingresa un numero "))

print("la tabla del 1 al 10 de su numero es ")


for i in range(10):
    print(numero, "x", i+1, "=", numero*(i+1))