

print("Hola Mundo!")
#definiendo una variable con camelCase
nombreCompleto = "Lucas Enriquez"
#definiendo una variable con snake_case (recomendado)
nombre_natural = "David Leiba"
#definiendo una variable
nombre = "Javier"

#este es un f-string un .function, es util cuando queremos definir datos como numeros o boleanos como una string, ya que todo ol reconoce como texto
#concatenar con f-string
bienvenida = f"hola {nombre} ¿como estas?"
#concatenar con +
bienvenida = "hola " + nombre + "¿como estas?"

#ahora si queremos que una variable no estes mas definida utilizamos un del, por ejemplo:_
del nombre_natural  #el -del- solo funciona antes de que la variable sea usada
#print(bienvenida), el print seria "hola 6 ¿como estas?" si la variable nombre fuera "nombre = 6"

# (in/not in) operadores de -pertenencia- se puede usar en el print para buscar si algo es true o false
#print("ola" in bienvenida) - seria true por que si bien ola como tal no existe si se encuentra en el codigo, hay que tener en cuenta que este es un lenguaje KEYSENSITIVE, por la tanto minusculas y mayusculas se reconocen como dos letras diferentes. 
#caso contrario fuera print("Max" in bienvenida) seria false ya que no existe ni siquiera dentro de otra palabra, dentro de la variable "bienvenida", ahora en cambio si tuvieramos print("Max" not in bienvenida) la respuesta seria true ya que efectivamnte no existe dentro de la variable bienvenida.

print("javier" in bienvenida) #True
print("javeir" not in bienvenida) #False