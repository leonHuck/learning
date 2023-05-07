""" Primer for: Almacenar en dos listas paralelas, nombres y sexos de 8 personas. 
Segundo for: Recorrerlas y guardar los nombres de las mujeres en una nueva lista. 
Mostrar los elementos de la lista resultante.
 """
nombres = []
sexos = []
nombresMujeres = []
for i in range(4):
    nombre = input('ingrese su nombre: ')
    nombres.append(nombre)
    sexo = input("ingrese su sexo: ")
    sexos.append(sexo)

for i in range(len(nombres)):
    if sexos[i] == "mujer":
        nombresMujeres.append(nombres[i]) 
print("los nombres de mujeres son: ", nombresMujeres)
 