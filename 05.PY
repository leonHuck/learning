""" Guardar en una lista los números pares mayores que 0 y menores que 31. 
 """
parMayor31 = []

hayMas = "si"
while hayMas == "si":
    numero = int(input("Ingrese un numero: "))
    if numero > 31 or numero % 2 == 0: 
        parMayor31.append(numero)
    hayMas = input("hay mas datos: (si/no)")
print("Numeros pares o mayores a 31 son: ", parMayor31)