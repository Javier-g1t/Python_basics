
with open("files\\texto_jv.txt", "w", encoding="UTF-8") as file:
    #sobreescribiendo el archivo 
    #file.write("jajajajajajaja")

    #agregando 2 lineas con writelines 
    file.writelines(["Hola maestro como andas\n", "misericordia\n"])

    #agregando otras 2 lineas 
    file.writelines(["hsgdkhkas andas\n", "miseriadskbhf"])