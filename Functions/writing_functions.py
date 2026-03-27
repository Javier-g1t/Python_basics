
#creando una funcion simple 
def saludar():
    print("Hola lucas, mi maestro ¿como andas?")

#ejecutando una funcion simple
def saludar(nombre,sexo):
    sexo = sexo.lower()
    if(sexo == "mujer"):
        adjetivo = "reina"
    elif(sexo == "hombre"):
        adjetivo = "maestro"
    else :
        adjetivo = "crack"

    print(f"Hola {nombre}, mi {adjetivo} ¿Como andas?")

saludar("Vania", "MUjer")
saludar("Mario", "hombre")
saludar("Axel", "none")

#creando una funcion que nos retorne multiples valores
def random_password(num):
    chars = "jhsdgvcjwndcl"
    num_int = str(num)
    num = int(num_int[0])
    c1 = num - 2 
    c2 = num
    c3 = num - 5
    password = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*42}"
    #para guardar un valor tengo que retornarlo con RETURN
    return password, num

#desempaquetando la funcion
pass_w, first_num = random_password(35)

#mostrando los resultados obtenidos y los datos utilizados para obtenerlo 
print(f"Tu contraseña nueva es: {pass_w}")
print(f"El numero utilizado para crearla fue : {first_num}")


