texto_bienvenida = "Bienvenido a este test sobre cuanto te gusta el queso :D"
print('\n'+texto_bienvenida.center(80, '-')+'\n')
opcion = input("""Pregunta 1: Que haces cuando ves una tabla de quesos?
               A) -Salgo corriendo
               B) -Pruebo uno de los quesos o incluso varios
               C) -No puedo evitar devorarla\n""")
puntuacion =0
if opcion == "A":
    puntuacion +=0

elif opcion == "B":
    puntuacion = puntuacion + 5

elif opcion == "C":
    puntuacion = puntuacion + 10
else:
    print("Las opciones posibles son A,B y C")
    exit()
    
    
opcion = input("""Pregunta 2: Como te gusta el queso?
               A) -Fresco
               B) -Maduro
               C) -Mozarella\n""")


if opcion == "A":
    puntuacion +=0

elif opcion == "B":
    puntuacion = puntuacion + 5

elif opcion == "C":
    puntuacion = puntuacion + 10
else:
    print("Las opciones posibles son A,B y C")
    exit()
    
if puntuacion>= 25:
    print(f"Tu puntuacion es: {puntuacion} Felicidades eres fanatico de los quesos")
elif puntuacion >=15:
    print(f"Tu puntuacion es: {puntuacion} Felicidades eres te gusta el queso")
else:
    print(f"Tu puntuacion es: {puntuacion} no te gustan los quesos")
    

