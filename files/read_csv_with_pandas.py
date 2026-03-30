import pandas as pd

#usando la funcion read_csv para leer el archivo CSV
df = pd.read_csv("files\\data.csv")
df2 = pd.read_csv("files\\data.csv")

#obteniendo los datos de la columna nombre
names = df["nombre"]

#ordenanadoel dataframe por la edad 
df_orden_ascendente = df.sort_values("edad")

#ordenandolo de forma descendente
df_orden_descendente = df.sort_values("edad", ascending = False)

#conacatenando los dos dataframes
df_concatenado = pd.concat([df,df2])

#accediendo a la primeras tres filas con head() 
primer_fila = df.head(3)

#accediendo a las ultimas 3 filas con tail()
ultimas_filas = df.tail(3)

#accediendo a la cantidad de filas y coluimnas con shape
filas_totales, columnas_totales = df.shape

#obteniendo data estadistica del dataframe
df_info = df.describe()

#accediendo a la edad de la fila 2
elemento_especifico_loc = df.loc[2, "edad"]

#accediendo a la edad de la fila 2 con iloc
elemento_especifico_iloc = df.iloc[2,2]

#accediendo a todas los apellidos con loc
apellidos = df.loc[:,"apellido"]

#accediendo a todas los apellidos con iloc
apellidos = df.iloc[:,1]

#accediendo a la fila 3 con loc 
file_3 = df.loc[2,:]

#accediendo a la fila 3 con iloc 
file_3 = df.iloc[2,:]

#acediendo a filas con edad mayor a 30 
mayor_que_30 = df.loc[df["edad"]>30, : ]


print(mayor_que_30)