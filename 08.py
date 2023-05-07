""" Cargar una lista con números. Invertir los elementos sin usar otra lista. 
 """

listaNumeros = []
hayMas = ""
while hayMas != "no":
    numero = int(input("Ingrese un numero: "))
    listaNumeros.append(numero)
    hayMas = input("hay mas datos: (si/no)")


for i in range(len(listaNumeros) // 2):
    aux = listaNumeros[i]
    listaNumeros[i] = listaNumeros[len(listaNumeros)-1-i]
    listaNumeros[len(listaNumeros)-1-i] = aux

print(listaNumeros)

