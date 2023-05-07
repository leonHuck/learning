""" Ingresar nombres en una lista, luego buscar un nombre y de encontrarlo decir en qué posición está. """

nombres = []

hayMas = "si"
while hayMas == "si":
    nombre = input("Ingrese su nombre: ")
    nombres.append(nombre)
    hayMas = input("hay mas datos: (si/no)")
buscarNombre = input("Que nombre desea buscar: ")
for i in range(len(nombres)):
    if buscarNombre == nombres[i]:
        print("la posicion de ", buscarNombre, "es ", i + 1)