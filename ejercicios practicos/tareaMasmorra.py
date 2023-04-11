import random
numWinner = random.randint(1,10)
titulo = "Bienbenido al juego de la mazzmorra elije las opciones que mejor te parescan para salir"
ganaste = "FELICIDADES SALISTE DE LA MASSMORRA\n GANASTE!!!!!!"
perdiste = "BUUU PERDISTE"
print("\n"+titulo+"\n") 
print("""Eres un aventurero intrépido que ha sido capturado por un malvado mago y encerrado en una masmorra. A tu alrededor, las paredes de piedra gris y los pasillos oscuros te hacen sentir atrapado y aislado. Pero eres astuto y valiente, y estás decidido a escapar de esta prisión.\n""")
opcion_escombros=input("Miras a tu alrededor y ves unos escombros quieres revisarlos?[S/N]\n")
if opcion_escombros=="S":
    print("\nrevisas los escombros y encontraste una piedra verde fosforecente y la guardaste en tu bolsillo, fuerzas la puerta y sales al pacillo\n")
    pierdaVerde=True
else:
    print("fuerzas la puerta y sales al pacillo")
    pierdaVerde = False

opcion_pasillo= input("Tienes dos opciones puedes seguir el camino de la derecha o de la izquierda [D/I]\n")

if opcion_pasillo=="D":
    opcion_guardias=input("\nte has encontrado con unos guardias quieres hablar con ellos y convencerles de que te dejen salir? [S/N]\n")
    if(opcion_guardias=="S" and pierdaVerde==True):
        print("\nlos guardias no te quieren ayudar porque no tienes nada a cambio pero les muestras la piedra verde y ellos aceptan te meten en un saco y te llevan hasta la salida\n")
        print(ganaste)
        exit()
    elif(opcion_guardias=="S" and pierdaVerde==False):
        print("\nlos guardias no te quieren ayudar porque no tienes nada a cambio y como no les ofreces nada ellos te mantan\n")
        print(perdiste)
        exit()
elif opcion_pasillo=="I":
    opcion_puerta=input("\ntomas el camino de la izquierda y te encuentras con una puerta cerra, la cual tiene un mecanismo de cerradura complicado que requiere una llave especial Buscas la llave en la avitacion de alado(B) o tratas de forzar la puerta (F)?\n")
    if opcion_puerta=="B":
        print("\nencutras la llave especial de la puerta de la anterior sala y vuelves a la habitacion de la puerta con crradura especial")
        opcion_llave=input("usas la llave(U) o fuerzas la puerta(F)\n")
        if opcion_llave=="U":
            print("la puerta se abre")
            print(f"Pero antes de salir tienes que contestar una pregunta cuanto es:5*{numWinner}\n")
            resultado=int(input("Cuanto es: "))
            if resultado == 5*numWinner:
                print(ganaste)
            else:
                print(perdiste)
    else:
        print(perdiste)
     
        
        


