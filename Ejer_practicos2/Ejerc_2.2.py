#creando una funcion que nos devuelva los numeros primos 
#entre 0 y el argumento que pasamos

#crear una funcion que verifique si un numero es primo
def is_prime(num):
    #verificamos que el numero pasado no pueda dividirse
    #por ningun numero entre 2 y ese mismo numero -1
    for i in range(2,num-1):
        #si es divisible por alguno retornamos false y termina el bucle
        if num%i==0: return False
    #si termina el bucle, significa que no fue divisible entonces es primo
    return True

#creando una funcion que retome una lista con todos los primos
def prime_upto(num):
    #creando la lista
    prime = []
    for i in range(3,num+1):
        #verificamos si el valor es primo
        result = is_prime(i)
        #en caso de que sea lo agregamos a la lista
        if result == True: prime.append(i)
    #devolvemos la lista 
    return prime
#creamos el resultado llamando a la funcion y lo mostramos
result = prime_upto(235)
print(result)