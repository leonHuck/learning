""" Cargar letras en una lista (while). Contar las vocales (for). Mostrar el total """

letras = []
masLetras = "si"
cantidadVocales = 0
while masLetras == 'si':
    letra = input("ingrese una letra: ")
    letras.append(letra)
    masLetras = input("Hay mas letras: ")
for letra in letras:
    if letra == "a" or letra  == "e" or letra == "i" or letra == "o" or letra  == "u":
        cantidadVocales = 1 + cantidadVocales
print("Cantidad de vocales: ", cantidadVocales)
print("las letras ingresadas son: ", letras)