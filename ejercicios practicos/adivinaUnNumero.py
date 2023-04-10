import random
numWinner = random.randint(1,10)
print("Adivina un numero del 1 al 10 para ganar")
numUser =int(input("Ingresa tu numero\n"))
if(numUser==numWinner):
    print("Enhorabuena haz a divinado el numero")
if(numUser>10):
    print("te haz pasado solo era del 1 al 10")
if(numUser<10):
    print("te haz quedado corto solo era del 1 al 10")
if(numUser!=numWinner):
    print("Que pena no haz adivinado el numero")

    
print(f"El numero ganador era: {numWinner}")