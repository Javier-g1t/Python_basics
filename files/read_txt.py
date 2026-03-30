
#usando open para abrir un archivo con una codificacion universal (UTF-8)
no_read_file = open("files\\texto_jv.txt",encoding="UTF-8")

#leer archivo completo 
#file = no_read_file.read()

#leer linea por linea 
#lines = no_read_file.readlines()

#leer una sola linea 
line = no_read_file.readline()

#cerrar el archivo 
no_read_file.close()

print(line)