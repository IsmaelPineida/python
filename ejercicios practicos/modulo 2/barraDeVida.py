from random import randint
import os
VIDA_INICIAL_PIKACHU = 80
VIDA_INICIAL_SQUIRTLE = 90
TAMANIO_BARRA_VIDA=10
vida_pikachu = VIDA_INICIAL_PIKACHU
vida_squirtle = VIDA_INICIAL_SQUIRTLE


while vida_pikachu > 0 and vida_squirtle > 0:
    # Se desenvuelven los turnos de combate

    # turno de pikachu
    print("Turno de Pikachu")
    ataque_pikachu = randint(1, 2)
    if ataque_pikachu == 1:
        # bola voltio
        print("Pikachu ataca con Bola Voltio")
        vida_squirtle -= 10
    else:
        print("Pikachu ataca con Onda trueno")
        vida_squirtle -= 11
    
    if vida_squirtle<0:
        vida_squirtle=0
    
    if vida_pikachu<0:
        vida_pikachu=0

    barras_de_vida_pikachu=int(vida_pikachu*TAMANIO_BARRA_VIDA/VIDA_INICIAL_PIKACHU)
    print("Pikachu:  [{}{}] ({}/{})".format("*"*barras_de_vida_pikachu," "*(TAMANIO_BARRA_VIDA-barras_de_vida_pikachu),vida_pikachu,VIDA_INICIAL_PIKACHU))
    barras_de_vida_squirtle=int(vida_squirtle*TAMANIO_BARRA_VIDA/VIDA_INICIAL_SQUIRTLE)
    print("Squirle:  [{}{}] ({}/{})".format("*"*barras_de_vida_squirtle," "*(TAMANIO_BARRA_VIDA-barras_de_vida_squirtle),vida_squirtle,VIDA_INICIAL_SQUIRTLE))
    
    
    
    
    #print(f"La vida de Pikachu es: {vida_pikachu}, la vida de Squirtle es: {vida_squirtle}")
    input("Enter para continuar....\n \n")
    os.system("cls")
    
    # turno squirtle
    print("Turno de Squirtle")
    ataque_squirtle = None
    while ataque_squirtle != "P" and ataque_squirtle != "A" and ataque_squirtle != "B" and ataque_squirtle!="N":
        ataque_squirtle = input(
            "¿Que ataque deseas realizar? [P]Placaje, [A]Pistola Agua,[B]Burbuja,[N]No Atacar:")
    if ataque_squirtle == "P":
        print("Squirtle ataca con Placaje")
        vida_pikachu -= 10
    elif ataque_squirtle == "A":
        print("Squirtle ataca con Pistola Agua")
        vida_pikachu -= 12
    elif ataque_squirtle == "B":
        print("Squirtle ataca con Burbuja")
        vida_pikachu -= 9
    elif ataque_squirtle=="N":
        print("Squirtle no ataca")
    
    if vida_squirtle<0:
        vida_squirtle=0
    
    if vida_pikachu<0:
        vida_pikachu=0


    barras_de_vida_pikachu=int(vida_pikachu*TAMANIO_BARRA_VIDA/VIDA_INICIAL_PIKACHU)
    print("Pikachu:  [{}{}] ({}/{})".format("*"*barras_de_vida_pikachu," "*(TAMANIO_BARRA_VIDA-barras_de_vida_pikachu),vida_pikachu,VIDA_INICIAL_PIKACHU))
    barras_de_vida_squirtle=int(vida_squirtle*TAMANIO_BARRA_VIDA/VIDA_INICIAL_SQUIRTLE)
    print("Squirle:  [{}{}] ({}/{})".format("*"*barras_de_vida_squirtle," "*(TAMANIO_BARRA_VIDA-barras_de_vida_squirtle),vida_squirtle,VIDA_INICIAL_SQUIRTLE))
    input("Enter para continuar\n \n")
    os.system("cls")
    
    
if vida_pikachu>vida_squirtle:
    print("Pikachu Gana")
else:
    print("Squirtle Gana")
    