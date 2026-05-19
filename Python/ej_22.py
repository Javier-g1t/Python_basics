#crear un programa que permita ingresar el nombre, el precio unitario y la cantidad de los n productos de una tienda. posteriormente calcule e imprima lo siguiente.
#un listado de los productos ingresados 
#la busqueda de un producto por su nombre, si lo encuentra muestra sus datos, si no lo encuentra debe indicarlo
#un listado de todos los productos queu su cantidad sea inferior a 10
#el total de dinero que recsudaria la tienda si es que vende todos sus productos


def producto():
    continuar = "si"
    while continuar == "si":
        nombre = input("ingrese un producto: ").capitalize()
        precio = int(input("ingrese el precio del producto: "))
        cantidad = int(input("ingrese la cantidad del producto: "))
        producto = (nombre,precio,cantidad)
        tienda.append(producto)
        continuar = input("desea continuar si/no ?: ")


def lista_productos():
    print("\n ---LISTA DE PRODUCTOS---")
    for i in tienda:
        print(f"{i[0]}") 


def buscar():
    print("\n ---BUSCADOR DE PRODUCTOS---")
    encontrado = True
    producto_buscado = input("Que producto desea buscar: ")
    for i in tienda:
        if producto_buscado == i[0]:
            encontrado = False
            print(f"{i[0]}, precio ${i[1]} tiene {i[2]} articulos")
            break
    if encontrado:
        print(f"{producto_buscado} no se encuentra regristrado")


def producto_bajo_stock():
    print("\n ---PRODUCTOS CON STOCK < 10 ---")
    for i in tienda:
        if i[2] < 10:
            print(f"{i[0]} - Cantidad: {i[2]}")

def total_dinero():
    total = 0
    for i in tienda:
        total += i[1] * i[2]
    print(f"\nTotal que recaudaría la tienda en total: ${total}")


tienda = []

producto()
lista_productos()
buscar()
producto_bajo_stock()
total_dinero()