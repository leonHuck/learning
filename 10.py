"""  Ingresar la lluvia caída en milímetros para cada día de la semana. 
Mostrar al final el total de lluvia caída y el nombre del día que más llovió. 
 """

semana = []
lluvia = []

hayMas = "si"
while hayMas == "si":
    day = input("Ingrese que dia de la semana es: ")
    rain = int(input("Ingrese cuanto llovio en milimetros: "))
    semana.append(day)
    lluvia.append(rain)
    hayMas = input("hay mas datos: (si/no)")

maxLluvia = 0
contador = 0
for i in range(len(lluvia)):
    contador = lluvia[i] + contador
print("El total de lluvia fue: ", contador)
for i in range(len(lluvia)):
    if lluvia[i] > maxLluvia:
        maxLluvia = lluvia[i]
        diaMax = semana[i]
print("Dia max lluvia: ", diaMax, maxLluvia)
