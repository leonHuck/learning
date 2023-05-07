""" Pedir nombres y sexo de personas y mostrar al final el total de mujeres y el nombre de cada una. """


personas = []
sexos = []
mujeres = []
hayMas = "si"
while hayMas == "si":
    nombre = input("Ingrese su nombre: ")
    sexo = input("Ingrese su sexo: ")
    personas.append(nombre)
    sexos.append(sexo)                        
    if sexo == "femenino":
        mujeres.append(nombre)
    hayMas = input("hay mas datos: (si/no)")

print("El total de mujeres es de: ",(len(mujeres)))
print("Los nombres de las mujeres son: ", mujeres)


    