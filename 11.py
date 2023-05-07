""" Cargar en listas los nombres y fechas de nacimiento de varias personas, 
luego recorrerlo y mostrar los nombres de los mayores de edad.
 """

aH = 2023
mH = 5
dH = 4
nombres = []
anos = []
meses = []
dias = []
hayMas = ""
while hayMas != "no":
    nombre = input("Ingrese su nombre: ")
    ano = int(input("Ingrese su ano de nacimiento: "))
    mes = int(input("Ingrese el mes de nacimiento: "))
    dia = int(input("Ingrese el dia que nacio: "))
    nombres.append(nombre)
    anos.append(ano)
    meses.append(mes)
    dias.append(dia)
    hayMas = input("hay mas datos: (si/no)")

for i in range(len(nombres)):
    if aH - anos[i] >= 18 and meses[i] - mH >= 0 and dias[i] - dH >= 0:
        print(nombres[i], "Usted es mayor")
    else:
        print(nombres[i], "Usted es menor")
