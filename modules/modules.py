
#importando un modulo asignandole el nombre "greet"
#import greet_module as grt

#tambien usando --import*-- podemos importar todo pero es una mala practica, por sobrecarga

#desde ese modulo, importamos dos funciones y les cambiamos el nombre 
from greet_module import greet as gr, weird_greet as wgreet
import greet_module as grt

#creamos las variables con los saludos 
greetings = gr("Lucas")
weird_greet = wgreet("Erika")

#mostramos los resultados
print(weird_greet)
print(greetings)

#para ver las propiedades y metodos de el namespace
#print(dir(grt))

#accedemos al nombre de este modulo
print(__name__)

#accedemos al nombre del modulo llamado 
#print(grt.__name__)





