
#abriendo el archivo con with open 
with open("files\\texto_jv.txt", encoding="UTF-8") as file:
    #leemos el archivo 
    content = file.read()

    #mostramos el archivo 
    print(content)

#no es necesario cerrarlo al usar el with open 