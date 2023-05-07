""" Eliminar todos los valores iguales de una lista. 
Previamente, solicitar el valor y si no está, mostrar un cartel diciendo que no lo ha encontrado.
 """

listaNumeros = []
hayMas = "si"
while hayMas == "si":
    numero = int(input("Ingrese un numero: "))
    listaNumeros.append(numero)
    hayMas = input("hay mas datos: (si/no)")
eliminarNumero = int(input("Que numero repetido desea eliminar: "))


for numero in listaNumeros:
    if eliminarNumero == numero:
        listaNumeros.remove(eliminarNumero)
        print(listaNumeros)
    
if eliminarNumero != numero:   
    print("No se encontro el numero buscado: ")
    print(listaNumeros)
    
