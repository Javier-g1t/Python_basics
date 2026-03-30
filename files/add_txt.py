with open("files\\texto_jv.txt", "a", encoding="UTF-8") as file:
    #usando un buvle para agregar varias lineas
    file.write("\n")
    for i in range(5):
        #agregando lineas 
        file.write(f"linea {i+1} agregada\n")