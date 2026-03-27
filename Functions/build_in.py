
#funciona con tuplas y conjuntos
numbers = [4,7,1,4,15]

#encontrando el numero mayor de una lista 
#funciona unicamente con numeros 
high_number = max(numbers)
print(f"el numero mayor es igual a {high_number}")

#encontrando el numero numero de una lista 
low_number = min(numbers)
print(f"el numero menor es igual a {low_number}")

#redondeando con round, agregando una coma al final podemos decidir cuntos decimales queremos 
number = round(12.4876278,5)

#retorna False -> 0, vacio ya sea lista/tupla/conjunto, False, ninguno/none \ True -> distinto a 0, True, cadena, datos no vacios 
bool_result = bool(0)

#retorna True, si todos los valores son verdaderos <> de 0, vacio, False, none
all_result = all([234, "true", [3344,23]]) 

#suma todos los valores de un iterable
total_sum = sum(numbers)

print(numbers)
print(total_sum)
