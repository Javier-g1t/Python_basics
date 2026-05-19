#8.	Crear un programa que permita a un usuario imprimir boletos de avión desde Valdivia a distintos puntos del país. Por cada boleto se ingresará:
#	Nombre del pasajero.
#	Destino del vuelo (1: Santiago, 2: Concepción, 3: Punta Arenas).(80,40,60)
#	Clase (e: ejecutiva; t: turista).
#Los siguientes son los valores de los vuelos para clase turista, según el destino la clase ejecutiva lleva un recargo de $20.000 en todos los destinos:



def nombre():
    return input("Ingrese el nombre del pasajero: ").strip().capitalize()


def destino():
    dest = input("Ingrese destino (santiago, concepcion, punta arenas): ").lower()
    
    if dest == "santiago":
        return 80000, dest
    elif dest == "concepcion":
        return 40000, dest
    elif dest == "punta arenas":
        return 60000, dest
    else:
        print("Destino inválido")
        return None, None


def clase(precio):
    cl = input("Ingrese la clase (ejecutivo/turista): ").lower()
    
    if cl == "ejecutivo":
        return precio + 20000, cl
    else:
        return precio, cl


def imprimir(nom, dest, cl, precio):
    print("\n--- BOLETO ---")
    print(f"Nombre: {nom}")
    print(f"Destino: {dest}")
    print(f"Clase: {cl}")
    print(f"Precio: ${precio}")


# PROGRAMA
nom = nombre()

precio_base, dest = destino()

if precio_base is not None:
    precio_final, cl = clase(precio_base)
    imprimir(nom, dest, cl, precio_final)