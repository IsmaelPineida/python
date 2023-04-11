#funcion para el menu
def menu():
    print("1. suma")
    print("2. resta")
    print("3. multiplicacion")
    print("4. division")
    print("0. salir")
    opcion =int(input("elija una opcion: "))
    return opcion

def solicitarDatos():
    num1= int(input("Ingrese el primer numero: "))
    num2= int(input("Ingrese el segundo numero: "))
    return num1, num2

def operaciones(operador, num1, num2):
    if(operador=="suma"):
        resultado=num1+num2
    elif(operador=="resta"):
        resultado=num1-num2
    elif(operador=="multiplica"):
        resultado=num1*num2
    elif(operador=="divide"):
        resultado=num1/num2
    return resultado
    
while True:
    opcion =menu()
    if (opcion==1):
        num1, num2 =solicitarDatos()
        print(f"el resultado de {num1}+{num2} es =")
        print(operaciones("suma",num1,num2))    
    elif (opcion==2):
        num1, num2 =solicitarDatos()
        print(f"el resultado de {num1}-{num2} es =")
        print(operaciones("resta",num1,num2))
    elif (opcion==3):
        num1, num2 =solicitarDatos()
        print(f"el resultado de {num1}x{num2} es =")
        print(operaciones("multiplica",num1,num2))
    elif (opcion==4):
        num1, num2 =solicitarDatos()
        print(f"el resultado de {num1}/{num2} es =")
        print(operaciones("divide",num1,num2))
    elif (opcion==0):
        break
    else:
        print("Ingrese una opcion valida")  
    print("\n")  

print("Salimos :D")