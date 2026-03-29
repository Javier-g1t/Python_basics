
#si el modulo dentro de una carperta en la misma ruta 
#import good_functions.greetings as m_greet

import sys
#Con sys.path poedmos saber donde esta ubicado el archivos en el compurtador
#print(sys.path) -> C:\\DEV\\Ciberseguridad\\Cursos\\Python_basics
sys.path.append("C:\\DEV\\Ciberseguridad\\Cursos\\Python_basics\\good_functions")

import greetings as greet
print(greet.greet("lucas"))