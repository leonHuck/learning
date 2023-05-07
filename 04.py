"""  Dada una lista con números, crear otra con los cuadrados de esos valores. 
 """

numeros = [2, 4, 5, 6, 10]
elevacion = []
numerosElevados = 0
for i in range(len(numeros)):
    numerosElevados = numeros[i]**2
    elevacion.append(numerosElevados)
print(elevacion) 




