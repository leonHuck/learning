""" Pedir el ingreso de 10 números. Contar los mayores de 23 y almacenar los que cumplen la condición. 
 Mostrar la cantidad y los números guardados.
 """
numeros = []
hayNumeros = 'si'
nMayores = 0 
for i in range(10):
    n = int(input("Ingrese un numero: "))
    numeros.append(n)
    if n > 23:
        nMayores = 1 + nMayores
print("La cantidad de numeros mayores a 23 son: ", nMayores)
print(numeros)
