""" Cargar en dos listas paralelas nombres y sueldos. 
Luego mostrar los nombres de las personas que ganan más de $185000.
 """

nombres = []
sueldos = []
hayMas = ""
while hayMas != "no":
    nombre = input("Ingrese su nombre: ")
    nombres.append(nombre)
    sueldo = int(input("Ingrese su sueldo: "))
    sueldos.append(sueldo)
    hayMas = input("hay mas datos: (si/no)")

for i in range(len(sueldos)):
    if sueldos[i] >= 185_000:
        print(nombres[i], "gana mas de 185.000.")
    