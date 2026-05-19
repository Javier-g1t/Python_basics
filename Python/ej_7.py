
#w = int(input("ingrese el valor de la variable W : "))

#if w == 1:
#    print("el ejercicio no tiene resultado en los reales")
#elif w == 0:
#    print("el ejercicio no tiene resultado en los reales")
#else:
#    x = ((w + 2)/(w - 1))+((3*w)/(w))
#    print(x) 

while True: 
    w = int(input("ingrese el valor de la variable W : "))

    if w == 0 or w == 1:
        print("el ejercicio no tiene resultado en los reales")
    else:
        x = ((w + 2)/(w - 1))+((3*w)/(w))
        print(f"Resultado {x}")
        break

