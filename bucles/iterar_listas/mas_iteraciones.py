
#creando las listas 
frutas = ["banana", "manzana", "ciruela", "pera", "naranja", "granada","durazno"]
cadena = "hola dalto"
numeros = [2,5,8,10]

#evitando que se coma una manzana con la sentencia continue 
for fruta in frutas:
    if fruta == "manzana":
        continue #sirve para saltea cuando la fruta sea igual al valor que le demos, no printea ese valor
    print(f"Me voy a comer una {fruta}")

#evitar que el bucle siga ejecuntandose (el else no se ejecuta tampoco cuando hay un break)
for fruta in frutas:
    print(f"Me voy a comer una {fruta}")
    if fruta == "pera":
        break
else:
    print("terminado")

#recorrer una cadena de texto
for letra in cadena:
    print(letra)

#for en forma larga
numeros_duplicados = list()
for numero in numeros:
    numeros_duplicados.append(numero * 2)

print(numeros_duplicados)

#for en una sola linea de codigo (duplicamos los numeros)
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)