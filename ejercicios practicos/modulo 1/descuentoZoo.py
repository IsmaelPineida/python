edad = int(input("digame su edad: "))
carnet = input("digame su tipo de carnet (E para estudiantes/ P Pensionista / F familia numerosa / N nada)")
if (25<=edad<=35 and carnet=="E")or edad < 10 or (edad>=65 and carnet =="P")or (carnet=="F"):
    print("se aplica descuento del 25%")
else:
    print("no se aplica el decuento")